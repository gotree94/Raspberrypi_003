# 라즈베리파이로 만드는 인공지능과 사물인터넷

## 챕터9. Yolo를 활용한 인공지능 객체인식

### 9.1 YOLOv8으로 객체 검출하기 285

* 회로 연결 285

| 라즈베리파이 핀 | 부품 | 
|:-------:|:-------:|
| GPIO 18 |  BUZZER |

```
# J8:
 🔴 3V3   (1)  (2)  🔴 5V
 🟢 GPIO2 (3)  (4)  🔴 5V
 🟢 GPIO3 (5)  (6)  ⚫ GND
 🟢 GPIO4 (7)  (8)  🟢 GPIO14
 👉⚫ GND   (9)  (10) 🟢 GPIO15
 🟢 GPIO17 (11) (12) 👉🟢 GPIO18
 🟢 GPIO27 (13) (14) ⚫ GND
 🟢 GPIO22 (15) (16) 🟢 GPIO23
 🔴 3V3  (17) (18) 🟢 GPIO24
 🟢 GPIO10 (19) (20) ⚫ GND
 🟢 GPIO9  (21) (22) 🟢 GPIO25
 🟢 GPIO11 (23) (24) 🟢 GPIO8
 ⚫ GND  (25) (26) 🟢 GPIO7
 🟢 GPIO0 (27) (28) 🟢 GPIO1
 🟢 GPIO5 (29) (30) ⚫ GND
 🟢 GPIO6 (31) (32) 🟢 GPIO12
 🟢 GPIO13 (33) (34) ⚫ GND
 🟢 GPIO19 (35) (36) 🟢 GPIO16
 🟢 GPIO26 (37) (38) 🟢 GPIO20
 ⚫ GND  (39) (40) 🟢 GPIO21
```

* 라이브러리 설치 286  

```
pip install torch opencv-python ultralytics --break-system-packages

1단계: 기존 torch 완전 제거
pip uninstall torch torchvision triton --break-system-packages -y

2단계: ARM CPU용 torch 설치 
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu --break-system-packages

3단계: 확인 
python3 -c "import torch; print(torch.__version__)"
```

```bash
admin@rp5-nwk:~/Raspberrypi_003/ai_iot $ pip install torch opencv-python ultralytics --break-system-packages
Defaulting to user installation because normal site-packages is not writeable
Collecting torch
  Downloading torch-2.11.0-cp313-cp313-manylinux_2_28_aarch64.whl.metadata (29 kB)
Collecting opencv-python
  Downloading opencv_python-4.13.0.92-cp37-abi3-manylinux_2_28_aarch64.whl.metadata (19 kB)
Collecting ultralytics
  Downloading ultralytics-8.4.26-py3-none-any.whl.metadata (39 kB)
Collecting filelock (from torch)
  Downloading filelock-3.25.2-py3-none-any.whl.metadata (2.0 kB)
Requirement already satisfied: typing-extensions>=4.10.0 in /usr/lib/python3/dist-packages (from torch) (4.13.2)
Requirement already satisfied: setuptools<82 in /usr/lib/python3/dist-packages (from torch) (78.1.1)
Collecting sympy>=1.13.3 (from torch)
  Downloading sympy-1.14.0-py3-none-any.whl.metadata (12 kB)
Collecting networkx>=2.5.1 (from torch)
  Downloading networkx-3.6.1-py3-none-any.whl.metadata (6.8 kB)
Requirement already satisfied: jinja2 in /usr/lib/python3/dist-packages (from torch) (3.1.6)
Collecting fsspec>=0.8.5 (from torch)
  Downloading fsspec-2026.2.0-py3-none-any.whl.metadata (10 kB)
Collecting cuda-toolkit==13.0.2 (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch)
  Downloading cuda_toolkit-13.0.2-py2.py3-none-any.whl.metadata (9.4 kB)
Collecting cuda-bindings<14,>=13.0.3 (from torch)
  Downloading cuda_bindings-13.2.0-cp313-cp313-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl.metadata (2.3 kB)
Collecting nvidia-cudnn-cu13==9.19.0.56 (from torch)
  Downloading nvidia_cudnn_cu13-9.19.0.56-py3-none-manylinux_2_27_aarch64.whl.metadata (1.9 kB)
Collecting nvidia-cusparselt-cu13==0.8.0 (from torch)
  Downloading nvidia_cusparselt_cu13-0.8.0-py3-none-manylinux2014_aarch64.whl.metadata (12 kB)
Collecting nvidia-nccl-cu13==2.28.9 (from torch)
  Downloading nvidia_nccl_cu13-2.28.9-py3-none-manylinux_2_18_aarch64.whl.metadata (2.0 kB)
Collecting nvidia-nvshmem-cu13==3.4.5 (from torch)
  Downloading nvidia_nvshmem_cu13-3.4.5-py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl.metadata (2.1 kB)
Collecting triton==3.6.0 (from torch)
  Downloading triton-3.6.0-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl.metadata (1.7 kB)
Collecting nvidia-cublas==13.1.0.3.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch)
  Downloading nvidia_cublas-13.1.0.3-py3-none-manylinux_2_27_aarch64.whl.metadata (1.7 kB)
Collecting nvidia-cuda-runtime==13.0.96.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch)
  Downloading nvidia_cuda_runtime-13.0.96-py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl.metadata (1.7 kB)
Collecting nvidia-cufft==12.0.0.61.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch)
  Downloading nvidia_cufft-12.0.0.61-py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl.metadata (1.8 kB)
Collecting nvidia-cufile==1.15.1.6.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch)
  Downloading nvidia_cufile-1.15.1.6-py3-none-manylinux_2_27_aarch64.whl.metadata (1.7 kB)
Collecting nvidia-cuda-cupti==13.0.85.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch)
  Downloading nvidia_cuda_cupti-13.0.85-py3-none-manylinux_2_25_aarch64.whl.metadata (1.7 kB)
Collecting nvidia-curand==10.4.0.35.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch)
  Downloading nvidia_curand-10.4.0.35-py3-none-manylinux_2_27_aarch64.whl.metadata (1.7 kB)
Collecting nvidia-cusolver==12.0.4.66.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch)
  Downloading nvidia_cusolver-12.0.4.66-py3-none-manylinux_2_27_aarch64.whl.metadata (1.8 kB)
Collecting nvidia-cusparse==12.6.3.3.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch)
  Downloading nvidia_cusparse-12.6.3.3-py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl.metadata (1.8 kB)
Collecting nvidia-nvjitlink==13.0.88.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch)
  Downloading nvidia_nvjitlink-13.0.88-py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl.metadata (1.7 kB)
Collecting nvidia-cuda-nvrtc==13.0.88.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch)
  Downloading nvidia_cuda_nvrtc-13.0.88-py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl.metadata (1.7 kB)
Collecting nvidia-nvtx==13.0.85.* (from cuda-toolkit[cublas,cudart,cufft,cufile,cupti,curand,cusolver,cusparse,nvjitlink,nvrtc,nvtx]==13.0.2; platform_system == "Linux"->torch)
  Downloading nvidia_nvtx-13.0.85-py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl.metadata (1.8 kB)
Collecting cuda-pathfinder~=1.1 (from cuda-bindings<14,>=13.0.3->torch)
  Downloading cuda_pathfinder-1.5.0-py3-none-any.whl.metadata (1.9 kB)
Requirement already satisfied: numpy>=2 in /usr/lib/python3/dist-packages (from opencv-python) (2.2.4)
Collecting matplotlib>=3.3.0 (from ultralytics)
  Downloading matplotlib-3.10.8-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl.metadata (52 kB)
Requirement already satisfied: pillow>=7.1.2 in /usr/lib/python3/dist-packages (from ultralytics) (11.1.0)
Requirement already satisfied: pyyaml>=5.3.1 in /usr/lib/python3/dist-packages (from ultralytics) (6.0.2)
Requirement already satisfied: requests>=2.23.0 in /usr/lib/python3/dist-packages (from ultralytics) (2.32.3)
Collecting scipy>=1.4.1 (from ultralytics)
  Downloading scipy-1.17.1-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl.metadata (62 kB)
Collecting torchvision>=0.9.0 (from ultralytics)
  Downloading torchvision-0.26.0-cp313-cp313-manylinux_2_28_aarch64.whl.metadata (5.5 kB)
Requirement already satisfied: psutil>=5.8.0 in /usr/lib/python3/dist-packages (from ultralytics) (7.0.0)
Collecting polars>=0.20.0 (from ultralytics)
  Downloading polars-1.39.3-py3-none-any.whl.metadata (10 kB)
Collecting ultralytics-thop>=2.0.18 (from ultralytics)
  Downloading ultralytics_thop-2.0.18-py3-none-any.whl.metadata (14 kB)
Collecting contourpy>=1.0.1 (from matplotlib>=3.3.0->ultralytics)
  Downloading contourpy-1.3.3-cp313-cp313-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl.metadata (5.5 kB)
Collecting cycler>=0.10 (from matplotlib>=3.3.0->ultralytics)
  Downloading cycler-0.12.1-py3-none-any.whl.metadata (3.8 kB)
Collecting fonttools>=4.22.0 (from matplotlib>=3.3.0->ultralytics)
  Downloading fonttools-4.62.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl.metadata (117 kB)
Collecting kiwisolver>=1.3.1 (from matplotlib>=3.3.0->ultralytics)
  Downloading kiwisolver-1.5.0-cp313-cp313-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl.metadata (5.1 kB)
Requirement already satisfied: packaging>=20.0 in /usr/lib/python3/dist-packages (from matplotlib>=3.3.0->ultralytics) (25.0)
Collecting pyparsing>=3 (from matplotlib>=3.3.0->ultralytics)
  Downloading pyparsing-3.3.2-py3-none-any.whl.metadata (5.8 kB)
Requirement already satisfied: python-dateutil>=2.7 in /usr/lib/python3/dist-packages (from matplotlib>=3.3.0->ultralytics) (2.9.0)
Collecting polars-runtime-32==1.39.3 (from polars>=0.20.0->ultralytics)
  Downloading polars_runtime_32-1.39.3-cp310-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl.metadata (1.5 kB)
Requirement already satisfied: charset_normalizer<4,>=2 in /usr/lib/python3/dist-packages (from requests>=2.23.0->ultralytics) (3.4.2)
Requirement already satisfied: idna<4,>=2.5 in /usr/lib/python3/dist-packages (from requests>=2.23.0->ultralytics) (3.10)
Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/lib/python3/dist-packages (from requests>=2.23.0->ultralytics) (2.3.0)
Requirement already satisfied: certifi>=2017.4.17 in /usr/lib/python3/dist-packages (from requests>=2.23.0->ultralytics) (2025.1.31)
Collecting mpmath<1.4,>=1.1.0 (from sympy>=1.13.3->torch)
  Downloading mpmath-1.3.0-py3-none-any.whl.metadata (8.6 kB)
Requirement already satisfied: MarkupSafe>=2.0 in /usr/lib/python3/dist-packages (from jinja2->torch) (2.1.5)
Downloading torch-2.11.0-cp313-cp313-manylinux_2_28_aarch64.whl (419.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 419.7/419.7 MB 4.2 MB/s eta 0:00:00
Downloading cuda_toolkit-13.0.2-py2.py3-none-any.whl (2.4 kB)
Downloading nvidia_cudnn_cu13-9.19.0.56-py3-none-manylinux_2_27_aarch64.whl (433.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 433.8/433.8 MB 3.9 MB/s eta 0:00:00
Downloading nvidia_cusparselt_cu13-0.8.0-py3-none-manylinux2014_aarch64.whl (220.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 220.8/220.8 MB 4.5 MB/s eta 0:00:00
Downloading nvidia_nccl_cu13-2.28.9-py3-none-manylinux_2_18_aarch64.whl (196.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 196.6/196.6 MB 4.6 MB/s eta 0:00:00
Downloading nvidia_nvshmem_cu13-3.4.5-py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl (60.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 60.2/60.2 MB 4.7 MB/s eta 0:00:00
Downloading triton-3.6.0-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl (176.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 176.1/176.1 MB 4.6 MB/s eta 0:00:00
Downloading cuda_bindings-13.2.0-cp313-cp313-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl (5.6 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.6/5.6 MB 4.5 MB/s eta 0:00:00
Downloading cuda_pathfinder-1.5.0-py3-none-any.whl (49 kB)
Downloading nvidia_cublas-13.1.0.3-py3-none-manylinux_2_27_aarch64.whl (542.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 542.9/542.9 MB 3.8 MB/s eta 0:00:00
Downloading nvidia_cuda_cupti-13.0.85-py3-none-manylinux_2_25_aarch64.whl (10.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 10.3/10.3 MB 5.1 MB/s eta 0:00:00
Downloading nvidia_cuda_nvrtc-13.0.88-py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl (43.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.0/43.0 MB 5.0 MB/s eta 0:00:00
Downloading nvidia_cuda_runtime-13.0.96-py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl (2.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 3.5 MB/s eta 0:00:00
Downloading nvidia_cufft-12.0.0.61-py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl (214.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 214.1/214.1 MB 4.5 MB/s eta 0:00:00
Downloading nvidia_cufile-1.15.1.6-py3-none-manylinux_2_27_aarch64.whl (1.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.1/1.1 MB 4.1 MB/s eta 0:00:00
Downloading nvidia_curand-10.4.0.35-py3-none-manylinux_2_27_aarch64.whl (62.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 62.0/62.0 MB 4.8 MB/s eta 0:00:00
Downloading nvidia_cusolver-12.0.4.66-py3-none-manylinux_2_27_aarch64.whl (223.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 223.5/223.5 MB 4.6 MB/s eta 0:00:00
Downloading nvidia_cusparse-12.6.3.3-py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl (162.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 162.2/162.2 MB 4.6 MB/s eta 0:00:00
Downloading nvidia_nvjitlink-13.0.88-py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl (38.8 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 38.8/38.8 MB 4.6 MB/s eta 0:00:00
Downloading nvidia_nvtx-13.0.85-py3-none-manylinux2014_aarch64.manylinux_2_17_aarch64.whl (148 kB)
Downloading opencv_python-4.13.0.92-cp37-abi3-manylinux_2_28_aarch64.whl (46.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 46.7/46.7 MB 4.8 MB/s eta 0:00:00
Downloading ultralytics-8.4.26-py3-none-any.whl (1.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.2/1.2 MB 4.6 MB/s eta 0:00:00
Downloading fsspec-2026.2.0-py3-none-any.whl (202 kB)
Downloading matplotlib-3.10.8-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl (9.5 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 9.5/9.5 MB 4.8 MB/s eta 0:00:00
Downloading contourpy-1.3.3-cp313-cp313-manylinux_2_26_aarch64.manylinux_2_28_aarch64.whl (334 kB)
Downloading cycler-0.12.1-py3-none-any.whl (8.3 kB)
Downloading fonttools-4.62.1-cp313-cp313-manylinux2014_aarch64.manylinux_2_17_aarch64.manylinux_2_28_aarch64.whl (5.0 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.0/5.0 MB 4.7 MB/s eta 0:00:00
Downloading kiwisolver-1.5.0-cp313-cp313-manylinux_2_24_aarch64.manylinux_2_28_aarch64.whl (1.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 1.3/1.3 MB 4.5 MB/s eta 0:00:00
Downloading networkx-3.6.1-py3-none-any.whl (2.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.1/2.1 MB 4.3 MB/s eta 0:00:00
Downloading polars-1.39.3-py3-none-any.whl (823 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 824.0/824.0 kB 4.1 MB/s eta 0:00:00
Downloading polars_runtime_32-1.39.3-cp310-abi3-manylinux_2_17_aarch64.manylinux2014_aarch64.whl (43.2 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 43.2/43.2 MB 4.8 MB/s eta 0:00:00
Downloading pyparsing-3.3.2-py3-none-any.whl (122 kB)
Downloading scipy-1.17.1-cp313-cp313-manylinux_2_27_aarch64.manylinux_2_28_aarch64.whl (32.9 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 32.9/32.9 MB 4.8 MB/s eta 0:00:00
Downloading sympy-1.14.0-py3-none-any.whl (6.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 6.3/6.3 MB 4.8 MB/s eta 0:00:00
Downloading mpmath-1.3.0-py3-none-any.whl (536 kB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 536.2/536.2 kB 3.8 MB/s eta 0:00:00
Downloading torchvision-0.26.0-cp313-cp313-manylinux_2_28_aarch64.whl (7.7 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.7/7.7 MB 4.8 MB/s eta 0:00:00
Downloading ultralytics_thop-2.0.18-py3-none-any.whl (28 kB)
Downloading filelock-3.25.2-py3-none-any.whl (26 kB)
Installing collected packages: nvidia-cusparselt-cu13, mpmath, cuda-toolkit, triton, sympy, scipy, pyparsing, polars-runtime-32, opencv-python, nvidia-nvtx, nvidia-nvshmem-cu13, nvidia-nvjitlink, nvidia-nccl-cu13, nvidia-curand, nvidia-cufile, nvidia-cuda-runtime, nvidia-cuda-nvrtc, nvidia-cuda-cupti, nvidia-cublas, networkx, kiwisolver, fsspec, fonttools, filelock, cycler, cuda-pathfinder, contourpy, polars, nvidia-cusparse, nvidia-cufft, nvidia-cudnn-cu13, matplotlib, cuda-bindings, nvidia-cusolver, torch, ultralytics-thop, torchvision, ultralytics
   ━━━╺━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  3/38 [triton]  WARNING: The scripts proton and proton-viewer are installed in '/home/admin/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
   ━━━━╺━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  4/38 [sympy]  WARNING: The script isympy is installed in '/home/admin/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
   ━━━━━━━━━━━━━━━━━━━━━━━╺━━━━━━━━━━━━━━━━ 22/38 [fonttools]  WARNING: The scripts fonttools, pyftmerge, pyftsubset and ttx are installed in '/home/admin/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━━━━ 34/38 [torch]  WARNING: The scripts torchfrtrace and torchrun are installed in '/home/admin/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╸━ 37/38 [ultralytics]  WARNING: The scripts ultralytics and yolo are installed in '/home/admin/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
types-seaborn 0.13.2 requires pandas-stubs, which is not installed.
Successfully installed contourpy-1.3.3 cuda-bindings-13.2.0 cuda-pathfinder-1.5.0 cuda-toolkit-13.0.2 cycler-0.12.1 filelock-3.25.2 fonttools-4.62.1 fsspec-2026.2.0 kiwisolver-1.5.0 matplotlib-3.10.8 mpmath-1.3.0 networkx-3.6.1 nvidia-cublas-13.1.0.3 nvidia-cuda-cupti-13.0.85 nvidia-cuda-nvrtc-13.0.88 nvidia-cuda-runtime-13.0.96 nvidia-cudnn-cu13-9.19.0.56 nvidia-cufft-12.0.0.61 nvidia-cufile-1.15.1.6 nvidia-curand-10.4.0.35 nvidia-cusolver-12.0.4.66 nvidia-cusparse-12.6.3.3 nvidia-cusparselt-cu13-0.8.0 nvidia-nccl-cu13-2.28.9 nvidia-nvjitlink-13.0.88 nvidia-nvshmem-cu13-3.4.5 nvidia-nvtx-13.0.85 opencv-python-4.13.0.92 polars-1.39.3 polars-runtime-32-1.39.3 pyparsing-3.3.2 scipy-1.17.1 sympy-1.14.0 torch-2.11.0 torchvision-0.26.0 triton-3.6.0 ultralytics-8.4.26 ultralytics-thop-2.0.18
admin@rp5-nwk:~/Raspberrypi_003/ai_iot $ pip uninstall torch torchvision triton --break-system-packages -y
Found existing installation: torch 2.11.0
Uninstalling torch-2.11.0:
  Successfully uninstalled torch-2.11.0
Found existing installation: torchvision 0.26.0
Uninstalling torchvision-0.26.0:
  Successfully uninstalled torchvision-0.26.0
Found existing installation: triton 3.6.0
Uninstalling triton-3.6.0:
  Successfully uninstalled triton-3.6.0
admin@rp5-nwk:~/Raspberrypi_003/ai_iot $ pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu --break-system-packages
Defaulting to user installation because normal site-packages is not writeable
Looking in indexes: https://download.pytorch.org/whl/cpu
Collecting torch
  Downloading https://download.pytorch.org/whl/cpu/torch-2.11.0%2Bcpu-cp313-cp313-manylinux_2_28_aarch64.whl.metadata (29 kB)
Collecting torchvision
  Downloading https://download-r2.pytorch.org/whl/cpu/torchvision-0.26.0%2Bcpu-cp313-cp313-manylinux_2_28_aarch64.whl.metadata (5.5 kB)
Requirement already satisfied: filelock in /home/admin/.local/lib/python3.13/site-packages (from torch) (3.25.2)
Requirement already satisfied: typing-extensions>=4.10.0 in /usr/lib/python3/dist-packages (from torch) (4.13.2)
Requirement already satisfied: setuptools<82 in /usr/lib/python3/dist-packages (from torch) (78.1.1)
Requirement already satisfied: sympy>=1.13.3 in /home/admin/.local/lib/python3.13/site-packages (from torch) (1.14.0)
Requirement already satisfied: networkx>=2.5.1 in /home/admin/.local/lib/python3.13/site-packages (from torch) (3.6.1)
Requirement already satisfied: jinja2 in /usr/lib/python3/dist-packages (from torch) (3.1.6)
Requirement already satisfied: fsspec>=0.8.5 in /home/admin/.local/lib/python3.13/site-packages (from torch) (2026.2.0)
Requirement already satisfied: numpy in /usr/lib/python3/dist-packages (from torchvision) (2.2.4)
Requirement already satisfied: pillow!=8.3.*,>=5.3.0 in /usr/lib/python3/dist-packages (from torchvision) (11.1.0)
Requirement already satisfied: mpmath<1.4,>=1.1.0 in /home/admin/.local/lib/python3.13/site-packages (from sympy>=1.13.3->torch) (1.3.0)
Requirement already satisfied: MarkupSafe>=2.0 in /usr/lib/python3/dist-packages (from jinja2->torch) (2.1.5)
Downloading https://download.pytorch.org/whl/cpu/torch-2.11.0%2Bcpu-cp313-cp313-manylinux_2_28_aarch64.whl (148.1 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 148.1/148.1 MB 5.1 MB/s eta 0:00:00
Downloading https://download-r2.pytorch.org/whl/cpu/torchvision-0.26.0%2Bcpu-cp313-cp313-manylinux_2_28_aarch64.whl (2.3 MB)
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 2.3/2.3 MB 4.9 MB/s eta 0:00:00
Installing collected packages: torch, torchvision
   ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 0/2 [torch]  WARNING: The scripts torchfrtrace and torchrun are installed in '/home/admin/.local/bin' which is not on PATH.
  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.
Successfully installed torch-2.11.0+cpu torchvision-0.26.0+cpu
admin@rp5-nwk:~/Raspberrypi_003/ai_iot $ python3 -c "import torch; print(torch.__version__)"
2.11.0+cpu
admin@rp5-nwk:~/Raspberrypi_003/ai_iot $

```

* 9_1_1 라이브러리 확인 286

```python
import cv2
import torch
import ultralytics
import numpy

print("cv2:", cv2.__version__)
print("torch:", torch.__version__)
print("ultralytics:", ultralytics.__version__)
print("numpy:", numpy.__version__)
```

* 9_1_2 기본 예제로 객체 검출하기 287  

```python
import cv2
from ultralytics import YOLO

def draw_detections(frame, results, names):
    if results is None:
        return frame
    for b in results.boxes:
        cls_id = int(b.cls.item())
        conf = float(b.conf.item())
        x1, y1, x2, y2 = map(int, b.xyxy[0].tolist())
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{names[cls_id]} {conf:.2f}"
        cv2.putText(
            frame,
            label,
            (x1, max(10, y1 - 6)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            1,
        )
    return frame

if __name__ == "__main__":
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise SystemExit("Camera open failed")

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            results = model(
                frame,
                imgsz=320,
                conf=0.5,
                iou=0.5,
                device="cpu",
            )[0]

            out = draw_detections(frame, results, model.names)
            cv2.imshow("YOLOv8 (OpenCV)", out)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
```


## 📌 YOLO v8에서 기본 예제로 제공되는 80개의 인식 리스트

| ID | Class           | ID | Class           | ID | Class           | ID | Class           | ID | Class           |
|----|----------------|----|----------------|----|----------------|----|----------------|----|----------------|
| 0  | person         | 1  | bicycle        | 2  | car            | 3  | motorcycle     | 4  | airplane       |
| 5  | bus            | 6  | train          | 7  | truck          | 8  | boat           | 9  | traffic light  |
| 10 | fire hydrant   | 11 | stop sign      | 12 | parking meter  | 13 | bench          | 14 | bird           |
| 15 | cat            | 16 | dog            | 17 | horse          | 18 | sheep          | 19 | cow            |
| 20 | elephant       | 21 | bear           | 22 | zebra          | 23 | giraffe        | 24 | backpack       |
| 25 | umbrella       | 26 | handbag        | 27 | tie            | 28 | suitcase       | 29 | frisbee        |
| 30 | skis           | 31 | snowboard      | 32 | sports ball    | 33 | kite           | 34 | baseball bat   |
| 35 | baseball glove | 36 | skateboard     | 37 | surfboard      | 38 | tennis racket  | 39 | bottle         |
| 40 | wine glass     | 41 | cup            | 42 | fork           | 43 | knife          | 44 | spoon          |
| 45 | bowl           | 46 | banana         | 47 | apple          | 48 | sandwich       | 49 | orange         |
| 50 | broccoli       | 51 | carrot         | 52 | hot dog        | 53 | pizza          | 54 | donut          |
| 55 | cake           | 56 | chair          | 57 | couch          | 58 | potted plant   | 59 | bed            |
| 60 | dining table   | 61 | toilet         | 62 | tv             | 63 | laptop         | 64 | mouse          |
| 65 | remote         | 66 | keyboard       | 67 | cell phone     | 68 | microwave      | 69 | oven           |
| 70 | toaster        | 71 | sink           | 72 | refrigerator   | 73 | book           | 74 | clock          |
| 75 | vase           | 76 | scissors       | 77 | teddy bear     | 78 | hair drier     | 79 | toothbrush     |


* 9_1_3 검출된 객체로 조건 설정하여 부저 울리기 291

```python
import cv2
from ultralytics import YOLO
from gpiozero import PWMOutputDevice
from time import sleep

buzzer = PWMOutputDevice(18)

def beep():
    buzzer.frequency = 440
    buzzer.value = 0.5
    sleep(0.3)
    buzzer.value = 0

def draw_detections(frame, results, names):
    if results is None:
        return frame
    for b in results.boxes:
        cls_id = int(b.cls.item())
        conf = float(b.conf.item())
        x1, y1, x2, y2 = map(int, b.xyxy[0].tolist())
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{names[cls_id]} {conf:.2f}"
        cv2.putText(
            frame,
            label,
            (x1, max(10, y1 - 6)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.5,
            (0, 255, 0),
            1,
        )
    return frame

if __name__ == "__main__":
    model = YOLO("yolov8n.pt")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise SystemExit("Camera open failed")

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            results = model(frame, imgsz=320, conf=0.5, iou=0.5, device="cpu")[0]

            person_detected = False
            for b in results.boxes:
                if int(b.cls.item()) == 0:
                    person_detected = True
                    break

            if person_detected:
                beep()

            out = draw_detections(frame, results, model.names)
            cv2.imshow("YOLOv8 (OpenCV)", out)

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    finally:
        buzzer.off()
        cap.release()
        cv2.destroyAllWindows()
```

### 9-2.사용자 모델 만들기 294

* 9_2_1 라즈베리파이에서 버튼을 눌러 사진 찍어 저장하기 294

```python
import os
from datetime import datetime
import cv2

SAVE_DIR = os.path.join(os.path.dirname(__file__), "pictures")
os.makedirs(SAVE_DIR, exist_ok=True)

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ok, image = cap.read()
        if not ok:
            break

        cv2.imshow("camera", image)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("s"):
            filename = datetime.now().strftime("%Y%m%d_%H%M%S_%f") + ".png"
            path = os.path.join(SAVE_DIR, filename)
            cv2.imwrite(path, image)
            print("saved:", path)
        elif key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
```

* 9_2_2 압축하기 296

```python
import os
import zipfile

def zip_pictures_folder():
    base_dir = os.path.dirname(__file__)
    pictures_dir = os.path.join(base_dir, "pictures")
    zip_path = os.path.join(base_dir, "pictures.zip")

    if not os.path.exists(pictures_dir):
        print("pictures folder not found.")
        return

    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(pictures_dir):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, pictures_dir)
                zipf.write(file_path, arcname)
    print(f"zip created: {zip_path}")

if __name__ == "__main__":
    zip_pictures_folder()
```


### 9.3 사용자 학습 모델 만들기 299
데이터 라벨링 299  

```python
import cv2
from ultralytics import YOLO

def draw_detections(frame, results, names):
    if results is None:
        return frame
    for b in results.boxes:
        cls_id = int(b.cls.item())
        conf = float(b.conf.item())
        x1, y1, x2, y2 = map(int, b.xyxy[0].tolist())
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{names[cls_id]} {conf:.2f}"
        cv2.putText(frame, label, (x1, max(10, y1 - 6)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    return frame

if __name__ == "__main__":
    model = YOLO("iot_model.pt")
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise SystemExit("Camera error")

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            results = model(frame, imgsz=320, conf=0.5, iou=0.5, device="cpu")[0]

            out = draw_detections(frame, results, model.names)
            cv2.imshow("YOLOv8", out)

            if cv2.waitKey(1) == ord('q'):
                break
    finally:
        cap.release()
        cv2.destroyAllWindows()
```

나만의 모델 만들기 (ultralytics hub) 311  

### 9.4 사용자 학습 모델 적용하여 객체 검출하기 320
회로 연결 320  
| 라즈베리파이 핀 | 부품 | 
|:-------:|:-------:|
| GPIO 4 |  LED1 |
| GPIO 17 |  LED2 |
| GPIO 27 |  LED3 |
| GPIO 22 |  LED4 |

```
# J8:
 🔴 3V3   (1)  (2)  🔴 5V
 🟢 GPIO2 (3)  (4)  🔴 5V
 🟢 GPIO3 (5)  (6)  ⚫ GND
 👉🟢 GPIO4 (7)  (8)  🟢 GPIO14
 👉⚫ GND   (9)  (10) 🟢 GPIO15
 👉🟢 GPIO17 (11) (12) 🟢 GPIO18
 👉🟢 GPIO27 (13) (14) ⚫ GND
 👉🟢 GPIO22 (15) (16) 🟢 GPIO23
 🔴 3V3  (17) (18) 🟢 GPIO24
 🟢 GPIO10 (19) (20) ⚫ GND
 🟢 GPIO9  (21) (22) 🟢 GPIO25
 🟢 GPIO11 (23) (24) 🟢 GPIO8
 ⚫ GND  (25) (26) 🟢 GPIO7
 🟢 GPIO0 (27) (28) 🟢 GPIO1
 🟢 GPIO5 (29) (30) ⚫ GND
 🟢 GPIO6 (31) (32) 🟢 GPIO12
 🟢 GPIO13 (33) (34) ⚫ GND
 🟢 GPIO19 (35) (36) 🟢 GPIO16
 🟢 GPIO26 (37) (38) 🟢 GPIO20
 ⚫ GND  (39) (40) 🟢 GPIO21
```
모델 파일 라즈베리파이로 이동 321  
내가 만든 모델로 객체 인식하기 322  

```python
import cv2
from ultralytics import YOLO
from gpiozero import LEDBoard
import time

def draw_detections(frame, results, names):
    if results is None:
        return frame
    for b in results.boxes:
        cls_id = int(b.cls.item())
        conf = float(b.conf.item())
        x1, y1, x2, y2 = map(int, b.xyxy[0].tolist())
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label = f"{names[cls_id]} {conf:.2f}"
        cv2.putText(frame, label, (x1, max(10, y1 - 6)),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)
    return frame

if __name__ == "__main__":
    model = YOLO("iot_model.pt")
    target_names = {"ultrasonic", "vr", "led", "ble"}

    leds = LEDBoard(4, 17, 27, 22)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise SystemExit("Camera error")

    try:
        while True:
            ok, frame = cap.read()
            if not ok:
                break

            results = model(frame, imgsz=320, conf=0.5, iou=0.5, device="cpu")[0]

            detected = any(
                model.names[int(b.cls.item())] in target_names
                for b in results.boxes
            )

            if detected:
                leds.on()
                time.sleep(0.2)
                leds.off()
                time.sleep(0.2)

            out = draw_detections(frame, results, model.names)
            cv2.imshow("YOLOv8", out)

            if cv2.waitKey(1) == ord('q'):
                break
    finally:
        leds.off()
        cap.release()
        cv2.destroyAllWindows()
```

객체가 검출되면 LED 깜빡이기 324  

</details>
