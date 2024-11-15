# NVIDIA NIM Factory

![nvidia-tensorrt-llm-engine](https://developer.download.nvidia.com/images/tensor-rt-llm-630x354.jpg)
This project is a factory for __NVIDIA NIM__ containers in which users/businesses can quantize many models and build their own __TensorRT-LLM engine__ for optimized inference. This enables users/businesses with large hardware resources but smaller business goals to save compute power by quantizing LLMs into different sizes. 

## Project Description
Over the past few years Generative AI models have popped up everywhere - from creating realistic responses to complex questions, to generating images and music to impress art critics around the globe. However, there are still some users or businesses who cannot use Generative AI due to limited resources, high cost for compute power or simply overweight their business goals. In this project, we enable them to quantize almost any AI model into different sizes and build an optimized inference engine using TensorRT-LLM. You will see how to quantize a model into one of the quantization format (*qformat*) such as *fp8, int4_sq, int4_awq* and many more.

From there, you will see how to build an inference engine using Nvidia TensorRT-LLM. If you are interested in more detailed explanation for building optimized inference engine, you can take a look at official documentation [here](https://nvidia.github.io/TensorRT-LLM/overview.html). After that, you might want to get your hands on your favourite AI model and quantize it to integrate into your own applications. What model it might be? Llama? Nemotron? Let's start immediately!

## System Requirements
- Operating System: Ubuntu 22.04
- CPU: None, tested with Intel Core i7 7th Gen CPU @ 2.30 GHz
- GPU requirements: Any NVIDIA training GPU, tested with 1x NVIDIA A100-80GB
- NVIDIA driver requirements: Latest driver version (with CUDA 12.2)
- Storage requirements: 40GB

# Quickstart
This section demonstrates how to use this project to run NVIDIA NIM Factory via NVIDIA AI Workbench. 

## Prerequisites

- Huggingface account: Get a username and token to download models. (some models might require access permission)
- Enough memory for storing downloaded models.

## Tutorial: build your own "NIM"
1. Install and configure AI Workbench locally and open up __AI Workbench__. Select a location of your choice.
2. Fork this repo into your own GitHub account.
3. __Inside AI Workbench:__
    - Click __Clone Project__ and enter the repo URL of your newly-forked repo.
    - AI Workbench will automatically clone the repo and build out the project environment, which can take several minutes to complete.
    - Upon `Build Complete`, select __Open Backend-app__ on the top right of the AI Workbench window, after that, select __Open Frontend-app__ to interact with application in browser.
4. __In the Frontend-app:__
   - Choose your desired family model, such as Llama, Nemotron, GPT, etc. 
   
