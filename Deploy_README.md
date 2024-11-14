## 安装Ollama

打开<https://ollama.com/download>下载**Ollama**，直接Install即可，但是**Ollama**在安装在c盘中。

如果你想要下载llama3到C盘外的话，可以通过配置**环境变量**。

​	首先打开高级系统设置，编辑系统变量，新建系统变量，设置变量名为**OLLAMA_MODELS**，设置变量值为**E:\OLLAMA**（下载到E盘OLLMA文件夹中，根据自己需求更改），然后重启即可。



## 安装llama3

终端运行：

```
ollama run llama3
```

程序自动下载 **Llama3** 的模型文件（8B)，下载完毕即可运行提问。



### 安装Node.js

打开<https://nodejs.org/zh-cn>下载即可。



## 部署WebUI

打开**Ollama_WebUI**文件夹中**main**文件夹的终端，执行以下命令部署：

```
npm install
npm run dev
```

出现以下界面即可：



