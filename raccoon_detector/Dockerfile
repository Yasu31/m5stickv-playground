FROM continuumio/miniconda3
WORKDIR /root
RUN git clone https://github.com/AIWintermuteAI/Yolo-digit-detector
WORKDIR Yolo-digit-detector
RUN git checkout e07b3080633a9a73253d36a0c9e47ece2a92f167
RUN conda create -y -n yolo python=3.6
# How to activate Conda environment in Dockerfile: https://pythonspeed.com/articles/activate-conda-dockerfile/
SHELL ["conda", "run", "-n", "yolo", "/bin/bash", "-c"]
RUN echo "The next step outputs nothing for a while, but let it sit for a few minutes and the pip install will be done"
RUN pip install -r requirements.txt
RUN pip install -e .

WORKDIR /root
RUN git clone https://github.com/datitran/raccoon_dataset
RUN mkdir data

RUN git clone https://github.com/sipeed/Maix_Toolbox
WORKDIR ./Maix_Toolbox
RUN bash get_nncase.sh
WORKDIR ./ncc
RUN tar xvf ncc-linux-x86_64.tar.xz
WORKDIR ../

WORKDIR /root