from huggingface_hub import snapshot_download


model_id=""
snapshot_download(repo_id=model_id, local_dir="Models/",
                  local_dir_use_symlinks=False, revision="main")