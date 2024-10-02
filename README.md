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
    - Upon `Build Complete`, select __Open Jupyterlab__ on the top right of the AI Workbench window, and the Jupyterlab app will open in a browser.
4. __In the Jupyterlab app:__
    - Execute 1st and 2nd cells:
      ```bash
      # install general requirements for TensorRT-LLM in code/TensorRT-LLM
      pip install -r code/TensorRT-LLM/requirements.txt
      # install requirements for particular model existing in examples folder (for ex. gpt)
      pip install -r code/TensorRT-LLM/examples/gpt/requirements.txt
      ```
   - To be able to quantize any model, we need to install additional dependencies in 3<sup>rd</sup>, 4<sup>th</sup> and 5<sup>th</sup> cells:
     ```bash
     pip install pickleshare
     pip install Cython
     cd code/TensorRT-LLM/examples/gpt
     ```
   - Download GPT2 model from Huggingface repo by executing 6<sup>th</sup> cell:
     ```bash
     mkdir -p ./gpt2 && git clone https://huggingface.co/openai-community/gpt2 ./gpt2
     ```
   - Start quantizing your model:
     ```bash
     # go to quantization directory
     cd ../quantization
     # make sure you installed dependencies for quant. again
     pip install -r requirements.txt
     # run quantization in int4_awq format
     %run quantize.py --model_dir ../gpt/gpt2 --qformat int4_awq --awq_block_size 64 --tp_size 1 --output_dir ../gpt/gpt2/gpt2_int4_awq
     ```
     __Note:__ All details about quantization [format](https://github.com/NVIDIA/TensorRT-LLM/tree/main/examples/quantization) and supported [models](https://nvidia.github.io/TensorRT-LLM/reference/support-matrix.html) can be found in official documentations.
   - __Build TensorRT-LLM engine__:
     ```bash
     # go to quantized model directory
     cd ../gpt
     # use Terminal for building TensorRT-LLM engine
     trtllm-build --checkpoint_dir gpt2/gpt2_int4_awq --output_dir gpt2/trtllm-engine-gpt2
     ```
     If you successfully build engine, you will see the output like:
     ```bash
     ......
     [03/12/2024-10:21:08] [TRT] [I] Engine generation completed in 35.9738 seconds.
     [03/12/2024-10:21:08] [TRT] [I] [MemUsageStats] Peak memory usage of TRT CPU/GPU memory allocators: CPU 212 MiB, GPU 775 MiB
     [03/12/2024-10:21:08] [TRT] [I] [MemUsageChange] TensorRT-managed allocation in building engine: CPU +0, GPU +775, now: CPU 0, GPU 775 (MiB)
     [03/12/2024-10:21:09] [TRT] [I] [MemUsageStats] Peak memory usage during Engine building and serialization: CPU: 6600 MiB
     [03/12/2024-10:21:09] [TRT-LLM] [I] Total time of building Unnamed Network 0: 00:00:36
     [03/12/2024-10:21:09] [TRT-LLM] [I] Serializing engine to gpt2/trtllm-engine-gpt2/trrank0.engine...
     [03/12/2024-10:21:11] [TRT-LLM] [I] Engine serialized. Total time: 00:00:02
     [03/12/2024-10:21:11] [TRT-LLM] [I] Total time of building all engines: 00:00:41
     ```
   - Lastly, you can run built engine for inferencing the quantized model:
     ```bash
     cd ..
     %run run.py --engine_dir gpt/gpt2/trtllm-engine-gpt2
     ```
     If the engines are run successfully, you will see output like:
     ```bash
     ......
     Input [Text 0]: "Born in north-east France, Soyer trained as a"
     Output [Text 0 Beam 0]: " chef before moving to London in the early"
     ```
     
# Summary

This project gives more customization on models for deployment than any other projects known up until now. __NVIDIA NIM__ containers are very great for users and businesses who wants to deploy them quickly and efficiently to the server(s). However, since NIM containers come with precompiled __TensorRT-LLM__ engine, it is impossible to quantize a model and build your own TensorRT-LLM engine inside NIMs. This project offers a solution for that and step-by-step instruction to accomplish your goals. __You can quickly build your own "NIM" and deploy it into your server(s)__.
