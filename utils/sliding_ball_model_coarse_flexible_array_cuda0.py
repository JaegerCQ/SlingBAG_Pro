import torch
from torch.nn import Parameter

class SlidingBallModel(torch.nn.Module):
    def __init__(self, xyz=None, pressure_0=None, radius=None): 
        super(SlidingBallModel, self).__init__()
        # 初始化为空的张量，用于存储三维空间中点的坐标、初始声压和半径。
        self._xyz = Parameter(torch.tensor(xyz, dtype=torch.float32) if xyz is not None else torch.empty(0))
        self._pressure_0 = Parameter(torch.tensor(pressure_0, dtype=torch.float32) if pressure_0 is not None else torch.empty(0))
        self._radius = Parameter(torch.tensor(radius, dtype=torch.float32) if radius is not None else torch.empty(0))
        self._is_destroyed = False  # 用于标记对象是否被销毁

    def initialize_attributes(self, xyz, pressure_0, radius):
        """初始化球的属性值"""
        self._xyz = Parameter(torch.tensor(xyz, dtype=torch.float32, requires_grad=True,device=torch.device('cuda:0')))
        self._pressure_0 = Parameter(torch.tensor(pressure_0, dtype=torch.float32, requires_grad=True,device=torch.device('cuda:0')))
        self._radius = Parameter(torch.tensor(radius, dtype=torch.float32, requires_grad=True,device=torch.device('cuda:0')))

    def get_attributes(self):
        """访问球的当前属性值"""
        if self._is_destroyed:
            return {'xyz': torch.empty(0), 'pressure_0': torch.empty(0), 'radius': torch.empty(0)}
        return {
            'xyz': self._xyz.clone(),
            'pressure_0': self._pressure_0.clone(),
            'radius': self._radius.clone()
        }

    def adaptive_density_optimization(self, pressure_threshold, radius_max_threshold, radius_min_threshold, mesh=None, boundaries=None):
        """自适应密度优化（新增mesh参数）"""            
        if self._pressure_0 < pressure_threshold or self._radius < radius_min_threshold or not batch_mesh_contains(self._xyz.unsqueeze(0), mesh)[0]:
            self._destroy()
            return None
        
        elif self._radius > radius_max_threshold:
            new_radius = self._radius / 2
            self._radius = Parameter(new_radius)#!!!!!!之前修改网格边界后，这句漏了！
            new_xyz = self._xyz + torch.tensor([self._radius.item(), 0, 0], dtype=torch.float32, device=self._xyz.device)
            
            # # 优先使用mesh判断
            # if mesh is not None:
            #     if not batch_mesh_contains(new_xyz.unsqueeze(0), mesh)[0]:
            #         return None
            # elif boundaries is not None:
            #     if self.is_out_of_bounds(boundaries, new_xyz):
            #         return None
            
            new_ball = self.__class__()
            new_ball.initialize_attributes(
                new_xyz.detach().cpu().numpy(),
                self._pressure_0.item(),
                new_radius.item()
            )
            return new_ball


    def clone_along_gradient(self, gradient_direction, mesh=None, boundaries=None):
        """沿梯度克隆（新增mesh参数）"""
        if not torch.is_tensor(gradient_direction):
            gradient_direction = torch.tensor(gradient_direction, dtype=torch.float32, device=self._xyz.device)
        
        new_xyz = self._xyz + gradient_direction
        
        # 优先使用mesh判断
        if mesh is not None:
            if not batch_mesh_contains(new_xyz.unsqueeze(0), mesh)[0]:
                return None
        elif boundaries is not None:
            if self.is_out_of_bounds(boundaries, new_xyz):
                return None
        
        new_ball = self.__class__()
        new_ball.initialize_attributes(
            new_xyz.detach().cpu().numpy(),
            self._pressure_0.item(),
            self._radius.item()
        )
        return new_ball

    def _destroy(self):
        self._is_destroyed = True

    def is_out_of_bounds(self, boundaries, xyz=None):
        """保留原有边界判断作为fallback"""
        if xyz is None:
            xyz = self._xyz
        x, y, z = xyz
        x_min, x_max, y_min, y_max, z_min, z_max = boundaries
        return not (x_min <= x <= x_max and y_min <= y <= y_max and z_min <= z <= z_max)

def batch_mesh_contains(points, mesh):
    """批量网格包含判断（新增函数）"""
    points_np = points.detach().cpu().numpy()
    return torch.tensor(mesh.contains(points_np), device=points.device)