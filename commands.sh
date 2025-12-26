DEBIAN_FRONTEND=noninteractive apt install -y python3-pip cuda-toolkit
pip install --upgrade pip
pip install uv
uv run --with vllm vllm --help
