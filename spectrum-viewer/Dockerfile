FROM python:3.6
RUN apk --update-cache \
    add musl \
    linux-headers \
    gcc \
    g++ \
    make 
RUN pip install --upgrade pip &&\
    pip install numpy \
                cffi \
                pysoundfile \
                librosa \
                scipy \
                flask \
                dash \
                plotly

COPY ./spectrogram_plot.py /usr/bin/spectrogram
RUN chmod +x /usr/bin/spectrogram
CMD ["/usr/bin/spectrogram"]

LABEL maintainer="spectrogram <ysugiura@mail.saitaam-u.ac.jp>" \
      description="Spectrogram Viewer" \
      description.ja="Spectrogram Viewer" \
      version="uplot:v2.0.0" \
      usage="docker run -d -p 8880:8880 spectrogram/spectrogram_plot"
