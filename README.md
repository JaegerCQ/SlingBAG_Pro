# SlingBAG Pro: Accelerating point cloud-based iterative reconstruction for 3D photoacoustic imaging under arbitrary array

[***ArXiv paper***](https://arxiv.org/abs/2407.11781)

High-quality three-dimensional (3D) photoacoustic imaging (PAI) is gaining increasing attention in clinical applications. To address the challenges of limited space and high costs, irregular geometric transducer arrays that conform to specific imaging regions are promising for achieving high-quality 3D PAI with fewer transducers. However, traditional iterative reconstruction algorithms struggle with irregular array configurations, suffering from high computational complexity, substantial memory requirements, and lengthy reconstruction times. In this work, we introduce SlingBAG Pro, an advanced reconstruction algorithm based on the point cloud iteration concept of the Sliding ball adaptive growth (SlingBAG) method, while extending its compatibility to arbitrary array geometries. SlingBAG Pro maintains high reconstruction quality, reduces the number of required transducers, and employs a hierarchical optimization strategy that combines zero-gradient filtering with progressively increased temporal sampling rates during iteration. This strategy rapidly removes redundant spatial point clouds, accelerates convergence, and significantly shortens overall reconstruction time. Compared to the original SlingBAG algorithm, SlingBAG Pro achieves up to a 2.2-fold speed improvement in point cloud-based 3D PA reconstruction under irregular array geometries. The proposed method is validated through both simulation and in vivo mouse experiments.  


## Guidance

The example in the provided codes is for the reconstruction of simulated hand vessel with 196 elements planar array (detailed in the article), if you want to reconstrut your own data, please replace the sensor location and sensor data files in the `train_196_elements_coarse_recon.ipynb` and `train_196_elements_fine_recon.ipynb`. Besides, the boundary set of the Gaussian balls should be modified carefully to match the reconstruction area. Sorry for all the inconvenience, we promise that the SlingBAG will soon be much more user-friendly, and we hope this guidance may help you. Good luck my friends!  
If you have any questions while using SlingBAG for 3D reconstruction, please be free to contact us. Best wishes!

## Installation

```bash
git clone https://github.com/JaegerCQ/SlingBAG.git
cd SlingBAG
```

```bash
conda create -n SlingBAG python=3.10 -y
conda activate SlingBAG
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```

```bash
pip install -r requirements.txt
```

Warning: for Windows, it needs `setuptools <= 72.1.0`; for Linux, it needs `gcc >= 9.1`.

## Usage

### Coarse reconstruction
Run `train_196_elements_coarse_recon.ipynb`.

### Fine reconstruction
Run `train_196_elements_fine_recon.ipynb`.

### Conversion from point cloud to voxel grid
Run `point_cloud_to_voxel_grid_shader.ipynb`.

## Tips
`utils/differentiable_rapid_raditor_kernel_v4_fine.cu` is the latest version of the CUDA kernel for the fine reconstruction stage. Compared to `utils/differentiable_rapid_raditor_kernel_v3_fine.cu`, it incorporates shared memory access, optimizes computational efficiency, and accelerates the reconstruction process. In `train_196_elements_fine_recon.ipynb`, simply replace `utils/differentiable_rapid_raditor_kernel_v3_fine.cu` with `utils/differentiable_rapid_raditor_kernel_v4_fine.cu` to use the updated version.

## BibTeX

```
@article{li2024slingbag,
  title={Sliding Gaussian ball adaptive growth (SlingBAG): point cloud-based iterative algorithm for large-scale 3D photoacoustic imaging},
  author={Li, Shuang and Wang, Yibing and Gao, Jian and Kim, Chulhong and Choi, Seongwook and Zhang, Yu and Chen, Qian and Yao, Yao and Li, Changhui},
  journal={arXiv preprint arXiv:2407.11781},
  year={2024}
}
```
