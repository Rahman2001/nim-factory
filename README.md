# NVIDIA NIM Factory

![nvidia-tensorrt-llm-engine](https://developer.download.nvidia.com/images/tensor-rt-llm-630x354.jpg)
This project is a factory for __NVIDIA NIM__ containers in which users/businesses can quantize many models and build their own __TensorRT-LLM engine__ for optimized inference. This enables users/businesses with large hardware resources but smaller business goals to save compute power by quantizing LLMs into different sizes. 

## Project Description
Over the past few years Generative AI models have popped up everywhere - from creating realistic responses to complex questions, to generating images and music to impress art critics around the globe. However, there are still some users or businesses who cannot use Generative AI due to limited resources, high cost for compute power or simply overweight their business goals. In this project, we enable them to quantize almost any AI model into different sizes and build an optimized inference engine using TensorRT-LLM. You will see how to quantize a model into one of the quantization format (*qformat*) such as *fp8, int4_sq, int4_awq* and many more.

From there, you will see how to build an inference engine using Nvidia TensorRT-LLM. If you are interested in more detailed explanation for building optimized inference engine, you can take a look at official documentation [here](https://nvidia.github.io/TensorRT-LLM/overview.html). After that, you might want to get your hands on your favourite AI model and quantize it to integrate into your own applications. What model it might be? Llama? Nemotron? Let's start immediately!

## System Requirements
- Operating System: Ubuntu 22.04
- CPU: None, tested with Intel Core i7 7th Gen CPU @ 2.30 GHz
- GPU requirements: Any NVIDIA training GPU, tested with 1x NVIDIA GTX-4GB
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
    - OR go to __Environment__ section of Workbench and start 1) __backend-app__ , after, 2) __frontend-app__ .
      ![environment tab](https://github.com/Rahman2001/nim-factory/blob/main/data/backend-app-start.PNG)
4. __In the Frontend-app:__
   - Choose your desired family model, such as _Llama, Nemotron, GPT_ etc. (__Note__: follow the order of tabs, for example, in our case, we chose "GPT" model family. After that, we are offered available model versions described in "Support Matrix" of TensorRT-LLM documentation.
     ![prepare_environment_page](https://github.com/Rahman2001/nim-factory/blob/main/data/prep_env_ui.PNG)
     Hugging Face credentials are optional as long as model repository will not require special permission as Llama does. So, make sure you obtained permission if you want to select Llama model family. After, click on __Prepare Environment__ button on the top middle. If everything gets installed successfully, we will see how __TensorRT-LLM__ text on the right side becomes green, otherwise, it will turn to red color.
   - Click on __TensorRT-LLM__ tab next to __Environment__ to proceed to our tensor operations.
     ![quantization_tab_page](https://github.com/Rahman2001/nim-factory/blob/main/data/quant_page_ui.PNG)
     Choose one of the available quantization format offered by TensorRT-LLM itself. In our case, we decided with _int4_awq_ format. Default values and their description are given for each parameter. (In the future, we will provide more range of parameters). After that, click on __Start Quantization__ button to start it and observe the __Quantization Window__ to know the progress of your operation. If quantization is successfull, we will see a model directory in our "models" folder, such as "_quant_gpt2_int4_awq_" folder and output at the end of the window as below:
     ```bash
     Inserted 147 quantizers
     Caching activation statistics for awq_lite...
     Searching awq_lite parameters...
     Padding vocab_embedding and lm_head for AWQ weights export
     current rank: 0, tp rank: 0, pp rank: 0
     ```
   - Next, click on __Build Engine__ tab to start building our inference engine.
     ![engine build page](https://github.com/Rahman2001/nim-factory/blob/main/data/build_engine_page_ui.PNG)
     __Note:__ parameter _max input lenght_ value must not exceed the value of _max_position_embeddings_ in _config.json_ file of the model, otherwise, you will get an error.
     After, click on __Start Engine Building__ to start the process. Watch closely the __Build Window__ if you get any error during build process. If engine builds successfully, you will see such output at the end:
     ```bash
     [03/12/2024-10:21:08] [TRT] [I] Engine generation completed in 35.9738 seconds.
     [03/12/2024-10:21:08] [TRT] [I] [MemUsageStats] Peak memory usage of TRT CPU/GPU memory allocators: CPU 212 MiB, GPU 775 MiB
     [03/12/2024-10:21:08] [TRT] [I] [MemUsageChange] TensorRT-managed allocation in building engine: CPU +0, GPU +775, now: CPU 0, GPU 775 (MiB)
     [03/12/2024-10:21:09] [TRT] [I] [MemUsageStats] Peak memory usage during Engine building and serialization: CPU: 6600 MiB
     [03/12/2024-10:21:09] [TRT-LLM] [I] Total time of building Unnamed Network 0: 00:00:36
     [03/12/2024-10:21:09] [TRT-LLM] [I] Serializing engine to trtllm_quant_gpt2_int4_awq/trtllm-engine/trrank0.engine...
     [03/12/2024-10:21:11] [TRT-LLM] [I] Engine serialized. Total time: 00:00:02
     [03/12/2024-10:21:11] [TRT-LLM] [I] Total time of building all engines: 00:00:41
     ```
   - After successfully downloading, quantizing model and building inference engine, paths of each model are saved in <code>model_paths.json</code> file which is located in <code>code/nim-factory-ui/backend</code> path of the project. In our case, our file should look like this:
     ```json
     {
          "base_models": {
              "gpt2": "/models/gpt2"
          },
     
          "quant_models": {
              "quant_gpt2_int4_awq": "/models/quant_gpt2_int4_awq"
          },
     
          "trtllm_engines": {
              "trtllm_quant_gpt2_int4_awq": "/models/trtllm_quant_gpt2_int4_awq"
          }
     }
     ```
     It can be used to track all the models when application is deployed to remote servers.
     
   - Here, you have to check your "__models__" folder for existence of inference engine which starts with "_trtllm_...". If it does, you can run the next command manually to interract with model:
     ```bash
     python3 run.py --engine_dir models/trtllm_quant_gpt2_int4_awq
     ```
     At the moment, __Run Engine__ tab is under active development which enables users to comfortably have a chat with their inference engine.

   ### YouTube demo
   Link: [video link](https://youtu.be/OOQtrP4gen4?si=Hal5_QHZLLKeUn5L)

   ## Summary

   This project is a demonstration of first steps to building your own "NIMs". A lot is required to do to improve the application, such as advanced error handling, enabling more features of TensorRT-LLM and more. We actively developing __Run Engine__ tab of the application to enable users to interact with built engine despite that we experience the hardware resource shortage at the moment. The application serves as a good stepping stone to those who want to discover the power of TensorRT libraries and take advantage of it.
