import argparse
from utils.utils_evaluation import smd_one_liner, smd_nn

def run_smd_one_liner():
    a, b, c = smd_one_liner(data_dir='data/', occlusion_intervals=1, occlusion_prob=0.0)
    print(a, b, c)

def run_smd_nn():
    a, b, c = smd_nn(data_dir='data/', occlusion_intervals=1, occlusion_prob=0.0)
    print(a, b, c)

if __name__ == "__main__":
    argparse = argparse.ArgumentParser()
    argparse.add_argument("--model", type=str, required=True, choices=["one_liner", "nn"])
    args = argparse.parse_args()

    if args.model == "one_liner":
        run_smd_one_liner()
    elif args.model == "nn":
        run_smd_nn()