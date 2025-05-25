import pickle

# 替换成你实际的路径
pkl_path = '/home/zhuzhuhao/haoran_proj/hiveformer/data/train_dataset/microsteps/seed0/close_box/variation0/variation_descriptions.pkl'

# 加载并打印内容
with open(pkl_path, 'rb') as f:
    data = pickle.load(f)

print("PKL 文件内容：")
print(data)

# 如果是字典或列表，可以更具体地打印
if isinstance(data, dict):
    for k, v in data.items():
        print(f"{k}: {v}")
elif isinstance(data, list):
    for i, v in enumerate(data):
        print(f"[{i}]: {v}")
