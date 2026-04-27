import os
import math

def get_simple_rms(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()
        if not data: return 0
        return sum(data) / len(data)

def check_files():
    ref_dir = "/app/reference"
    gen_dir = "/app/separated/htdemucs/lp_numb_test"
    files = ["vocals.wav", "drums.wav", "bass.wav", "other.wav"]

    print("\n" + "=" * 30)
    print("ТЕСТЫ")
    print("=" * 30)

    for name in files:
        ref = os.path.join(ref_dir, name)
        gen = os.path.join(gen_dir, name)

        if not os.path.exists(ref) or not os.path.exists(gen):
            print(f"{name}: ФАЙЛ НЕ НАЙДЕН")
            continue

        rms_ref = get_simple_rms(ref)
        rms_gen = get_simple_rms(gen)

        if math.isclose(rms_ref, rms_gen, rel_tol=0.08):
            print(f"{name}: ✅ ОК")
        else:
            diff = abs(rms_ref - rms_gen)
            print(f"{name}: ❌ ОШИБКА (Слишком большая разница: {diff:.4f})")

if __name__ == "__main__":
    check_files()