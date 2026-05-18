import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            ".."
        )
    )
)

from app.preprocessing.dataset_loader import X, y


print("X Shape:", X.shape)
print("y Shape:", y.shape)

print("Sample Labels:")
print(y[:10])