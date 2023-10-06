FROM pytorch/pytorch:2.1.0-cuda11.8-cudnn8-runtime

# Set directory
WORKDIR /workspace
COPY . /workspace

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "src/run_dghl.py", "--random_seed", "1", "--experiment_name", "'DGHL'", "--occlusion_intervals", "5", "--occlusion_prob", "0"]
