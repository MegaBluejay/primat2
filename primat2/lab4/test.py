import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import learning_curve, train_test_split
from sklearn.metrics import make_scorer
from sklearn.preprocessing import StandardScaler
from sklearn.svm import NuSVC

from .gen import generate
from .metrics import metrics

res_dir = str(Path(__file__).parent.resolve() / "res")
sys.stdout = open(f"{res_dir}/text", "w")

Xog, y = generate(10_000)
X = StandardScaler().fit_transform(Xog)
Xog_train, Xog_test, X_train, X_test, y_train, y_test = train_test_split(Xog, X, y)

xx, yy = np.meshgrid(np.linspace(-1, 1, 100), np.linspace(-1, 1, 100))


def do_ac(kernel="rbf", nu=0.25):
    svc = NuSVC(kernel=kernel, nu=nu)
    svc.fit(X_train, y_train)
    y_pred = svc.predict(X_test)

    print(f"{kernel=}, {nu=}")
    for name, metric in metrics.items():
        print(f"  {name}={metric(y_test, y_pred)}")
    print()

    plt.plot(Xog_test[y_pred, 0], Xog_test[y_pred, 1], "ro")
    plt.plot(Xog_test[~y_pred, 0], Xog_test[~y_pred, 1], "bo")
    plt.savefig(f"{res_dir}/ac_points_{kernel}_{nu}.png")
    plt.clf()

    fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
    z = svc.decision_function(np.c_[xx.ravel(), yy.ravel()]).reshape(xx.shape)
    ax.plot_surface(xx, yy, z)
    plt.savefig(f"{res_dir}/ac_surface_{kernel}_{nu}.png")
    plt.clf()


for kernel in ["linear", "poly", "rbf", "sigmoid"]:
    do_ac(kernel=kernel)
for nu in [0.05, 0.2, 0.3]:
    do_ac(nu=nu)

for name, metric in metrics.items():
    train_sizes, train_scores, test_scores = learning_curve(
        NuSVC(kernel="rbf", nu=0.25),
        X,
        y,
        cv=3,
        scoring=make_scorer(metric),
        train_sizes=[10, 50, 100, 500, 1000, 5000],
    )
    plt.plot(train_sizes, np.mean(train_scores, axis=1))
    plt.plot(train_sizes, np.mean(test_scores, axis=1))
    plt.savefig(f"{res_dir}/b_{name}.png")
    plt.clf()

sys.stdout.close()
