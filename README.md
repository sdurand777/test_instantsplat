## Get Started

### Installation
1. Clone InstantSplat and download pre-trained model.
```bash
git clone --recursive https://github.com/NVlabs/InstantSplat.git
cd InstantSplat
git submodule update --init --recursive
cd submodules/dust3r/
mkdir -p checkpoints/
wget https://download.europe.naverlabs.com/ComputerVision/DUSt3R/DUSt3R_ViTLarge_BaseDecoder_512_dpt.pth -P checkpoints/
cd ../../
```

2. Create the environment (or use pre-built docker), here we show an example using conda.
```bash
conda create -n instantsplat python=3.11 cmake=3.14.0
conda activate instantsplat
conda install pytorch torchvision pytorch-cuda=12.1 -c pytorch -c nvidia  # use the correct version of cuda for your system
pip install -r requirements.txt
pip install submodules/simple-knn
# modify the rasterizer
vim submodules/diff-gaussian-rasterization/cuda_rasterizer/auxiliary.h
'p_view.z <= 0.2f' -> 'p_view.z <= 0.001f' # line 154
pip install submodules/diff-gaussian-rasterization
```

3. Optional but highly suggested, compile the cuda kernels for RoPE (as in CroCo v2).
```bash
# DUST3R relies on RoPE positional embeddings for which you can compile some cuda kernels for faster runtime.
cd submodules/dust3r/croco/models/curope/
python setup.py build_ext --inplace
```

### Usage
1. Data preparation (Our pre-processed data: [link](https://drive.google.com/file/d/1Z17tIgufz7-eZ-W0md_jUlxq89CD1e5s/view))
```bash
  cd <data_path>
  # then do whatever data preparation
```

2. Command
```bash
  # InstantSplat train and output video (no GT reference, render by interpolation) using the following command.
  bash scripts/run_train_infer.sh

  # InstantSplat train and evaluate (with GT reference) using the following command.
  bash scripts/run_train_eval.sh
```
``
