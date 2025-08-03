# SlingBAG Pro: Accelerating point cloud-based iterative reconstruction for 3D photoacoustic imaging under arbitrary array

[***ArXiv paper***](https://arxiv.org/abs/2407.11781)

High-quality three-dimensional (3D) photoacoustic imaging (PAI) is gaining increasing attention in clinical applications. To address the challenges of limited space and high costs, irregular geometric transducer arrays that conform to specific imaging regions are promising for achieving high-quality 3D PAI with fewer transducers. However, traditional iterative reconstruction algorithms struggle with irregular array configurations, suffering from high computational complexity, substantial memory requirements, and lengthy reconstruction times. In this work, we introduce SlingBAG Pro, an advanced reconstruction algorithm based on the point cloud iteration concept of the Sliding ball adaptive growth (SlingBAG) method, while extending its compatibility to arbitrary array geometries. SlingBAG Pro maintains high reconstruction quality, reduces the number of required transducers, and employs a hierarchical optimization strategy that combines zero-gradient filtering with progressively increased temporal sampling rates during iteration. This strategy rapidly removes redundant spatial point clouds, accelerates convergence, and significantly shortens overall reconstruction time. Compared to the original SlingBAG algorithm, SlingBAG Pro achieves up to a 2.2-fold speed improvement in point cloud-based 3D PA reconstruction under irregular array geometries. The proposed method is validated through both simulation and in vivo mouse experiments.  

![image](https://github.com/JaegerCQ/SlingBAG_Pro/blob/main/fig/SlingBAG_Pro_Pipeline.png)   
_The overall framework of SlingBAG Pro iterative reconstruction algorithm for 3D PAI under arbitrary array. (a) The SlingBAG Pro pipeline. (b) Principle of zero-gradient filtering for refinement of point cloud initialization. (c) Hierarchical optimization based on variable sampling rates. (d) Adaptive growth optimization in coarse and fine reconstruction stage._

## Simulation results

![image](https://github.com/JaegerCQ/SlingBAG_Pro/blob/main/fig/hand_vessel_SlingBAG_Pro.png)   
_Comparison of 3D photoacoustic reconstruction results under sparse irregular arrays. (a) Top-view maximum amplitude projection (MAP), front-view MAP, and the cross-sectional slice along the green dashed line in the top-view MAP of the acoustic source. (b) Top-view MAP, front-view MAP, and corresponding cross-sectional slice along the green dashed line in the top-view MAP of the UBP reconstruction results with 505, 1009, 2006 sensors, respectively. (c) Top-view MAP, front-view MAP, and corresponding cross-sectional slice along the green dashed line in the top-view MAP of the SlingBAG Pro reconstruction results with 505, 1009, 2006 sensors, respectively. (d) Imaging setup. (e) Point cloud iteration process of SlingBAG Pro reconstruction with 2006 sensors. (Scale bar: 10 mm.)_

## Guidance

The example in the provided codes is for the reconstruction of simulated hand vessel with 2006 elements irregular array (detailed in the article), if you want to reconstrut your own data, please replace the sensor location and sensor data files in the `train_phantom_finger_coarse_Hierarchical_2006.ipynb`, `train_phantom_finger_fine_Hierarchical_2006.ipynb` and `train_phantom_finger_fine_softplus_2006.ipynb`. Sorry for all the inconvenience, we promise that the SlingBAG will soon be much more user-friendly, and we hope this guidance may help you. Good luck my friends!  
If you have any questions while using SlingBAG_Pro for 3D reconstruction under arbitrary array, please be free to contact us. Best wishes!

## Installation

```bash
git clone https://github.com/JaegerCQ/SlingBAG_Pro.git
cd SlingBAG_Pro
```

```bash
conda create -n SlingBAG_Pro python=3.10 -y
conda activate SlingBAG_Pro
conda install pytorch torchvision torchaudio pytorch-cuda=11.8 -c pytorch -c nvidia
```

```bash
pip install -r requirements.txt
```

Warning: for Windows, it needs `setuptools <= 72.1.0`; for Linux, it needs `gcc >= 9.1`.

## Usage

### Coarse reconstruction
Run `train_phantom_finger_coarse_Hierarchical_2006.ipynb`.

### Fine reconstruction
Run `train_phantom_finger_fine_Hierarchical_2006.ipynb`. Then run `train_phantom_finger_fine_softplus_2006.ipynb` to further refine the result.

### Conversion from point cloud to voxel grid
Run `volume_rendering_gpu_0.2e-3_cuda0_softplus.ipynb`.

## BibTeX

```
@article{li2024slingbag,
  title={Sliding Gaussian ball adaptive growth (SlingBAG): point cloud-based iterative algorithm for large-scale 3D photoacoustic imaging},
  author={Li, Shuang and Wang, Yibing and Gao, Jian and Kim, Chulhong and Choi, Seongwook and Zhang, Yu and Chen, Qian and Yao, Yao and Li, Changhui},
  journal={arXiv preprint arXiv:2407.11781},
  year={2024}
}
```
