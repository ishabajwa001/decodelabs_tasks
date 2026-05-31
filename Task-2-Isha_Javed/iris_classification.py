# Importing necessary libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import warnings
warnings.filterwarnings("ignore")

from sklearn.datasets          import load_iris
from sklearn.model_selection   import train_test_split, cross_val_score, StratifiedKFold
from sklearn.preprocessing     import StandardScaler
from sklearn.neighbors         import KNeighborsClassifier
from sklearn.tree              import DecisionTreeClassifier
from sklearn.linear_model      import LogisticRegression
from sklearn.metrics           import (
    confusion_matrix, classification_report,
    f1_score, accuracy_score, ConfusionMatrixDisplay,
)

print("=" * 90)
print("                     Iris Flower Classification Using AI")
print("                     KNN + Algorithm Comparison +")
print("                     Cross-Validation + Custom Prediction")
print("=" * 90)


# Step 1 – Load Dataset
print("\nSTEP 1: Loading Iris Dataset...")

iris        = load_iris()
X           = iris.data
y           = iris.target
features    = iris.feature_names
class_names = iris.target_names

df = pd.DataFrame(X, columns=features)
df["species"] = [class_names[i] for i in y]

print(f"  Samples    : {X.shape[0]}")
print(f"  Features   : {X.shape[1]}  → {list(features)}")
print(f"  Classes    : {len(class_names)}  → {list(class_names)}")
print(f"  Per class  : {dict(zip(class_names, np.bincount(y)))}")
print("\n  First 5 rows:")
print(df.head().to_string(index=False))


# Step 2 – Split and Scale
print("\nSTEP 2:  Splitting (80/20) and Scaling Features...")

X_train_raw, X_test_raw, y_train, y_test = train_test_split(
    X, y,
    test_size    = 0.20,
    random_state = 42,
    shuffle      = True,
    stratify     = y
)

scaler  = StandardScaler()
X_train = scaler.fit_transform(X_train_raw)
X_test  = scaler.transform(X_test_raw)

print(f"  Train : {X_train.shape[0]} samples  |  Test : {X_test.shape[0]} samples")
print(f"  Scaled mean ≈ {X_train.mean(axis=0).round(3)}")
print(f"  Scaled std  ≈ {X_train.std(axis=0).round(3)}")


# Step 3 – Elbow Method for Optimal K
print("\nSTEP 3: Finding Optimal K via Elbow Method...")

error_rates = []
k_range     = range(1, 31)

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    error_rates.append(1 - accuracy_score(y_test, preds))

optimal_k = list(k_range)[np.argmin(error_rates)]
print(f"  Optimal K = {optimal_k}  (error rate = {min(error_rates):.4f})")


# Step 4 – Train KNN with Optimal K
print(f"\nSTEP 4: Training KNN (K={optimal_k})...")

knn_model   = KNeighborsClassifier(n_neighbors=optimal_k)
knn_model.fit(X_train, y_train)
knn_preds   = knn_model.predict(X_test)

knn_acc = accuracy_score(y_test, knn_preds)
knn_f1  = f1_score(y_test, knn_preds, average="weighted")
knn_cm  = confusion_matrix(y_test, knn_preds)

print(f"  Accuracy : {knn_acc*100:.2f}%   |   F1 Score : {knn_f1:.4f}")
print("\n  Classification Report:")
print(classification_report(y_test, knn_preds, target_names=class_names))


# Step 5 – Compare with Decision Tree and Logistic Regression
print("\nSTEP 5: Comparing Algorithms...")
print(f"  {'Algorithm':<25} {'Accuracy':>10} {'F1 Score':>10}")
print(f"  {'-'*47}")

algorithms = {
    f"KNN (K={optimal_k})"    : KNeighborsClassifier(n_neighbors=optimal_k),
    "Decision Tree"            : DecisionTreeClassifier(random_state=42),
    "Logistic Regression"      : LogisticRegression(max_iter=200, random_state=42),
}

results = {}

for name, clf in algorithms.items():
    clf.fit(X_train, y_train)
    preds = clf.predict(X_test)
    acc   = accuracy_score(y_test, preds)
    f1    = f1_score(y_test, preds, average="weighted")
    results[name] = {"model": clf, "acc": acc, "f1": f1, "preds": preds}
    print(f"  {name:<25} {acc*100:>9.2f}%  {f1:>10.4f}")

best_algo = max(results, key=lambda n: results[n]["f1"])
print(f"\n  -> Best Algorithm : {best_algo}  (F1 = {results[best_algo]['f1']:.4f})")


# Step 6 – 5-Fold Cross-Validation
print("\nSTEP 6: Running 5-Fold Cross-Validation...")
print(f"  {'Algorithm':<25} {'CV Mean':>10} {'CV Std':>10} {'Min':>8} {'Max':>8}")
print(f"  {'-'*65}")

cv_results = {}

for name, clf in algorithms.items():
    skf    = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
    scores = cross_val_score(clf, X_train, y_train,
                            cv=skf, scoring="f1_weighted")
    cv_results[name] = scores
    print(f"  {name:<25} {scores.mean():>10.4f} {scores.std():>10.4f}"
        f" {scores.min():>8.4f} {scores.max():>8.4f}")

print("\n  -> Model is consistent, not just lucky on one split.")


# Step 7 – Custom Input Prediction
print("\nSTEP 7: Custom Input Prediction...")

custom_flowers = np.array([
    [5.1, 3.5, 1.4, 0.2],
    [6.0, 2.9, 4.5, 1.5],
    [6.7, 3.0, 5.5, 2.1],
])

custom_scaled = scaler.transform(custom_flowers)

print(f"\n  {'Flower':<8} {'Sepal L':>8} {'Sepal W':>8} "
    f"{'Petal L':>8} {'Petal W':>8}   {'Predicted':<14} {'Confidence'}")
print(f"  {'-'*70}")

for i, (flower, scaled) in enumerate(zip(custom_flowers, custom_scaled)):
    pred_class = knn_model.predict([scaled])[0]
    proba      = knn_model.predict_proba([scaled])[0]
    confidence = proba[pred_class] * 100
    species    = class_names[pred_class]
    print(f"  Flower {i+1}  "
        f"{flower[0]:>8.1f} {flower[1]:>8.1f} "
        f"{flower[2]:>8.1f} {flower[3]:>8.1f}   "
        f"{species:<14} {confidence:.0f}%")


# Step 8 – Build Visualisation Dashboard
print("\nSTEP 8: Building Visualisation Dashboard...")

plt.style.use("seaborn-v0_8-paper")
plt.rcParams.update({
    "font.family"      : "DejaVu Sans",
    "axes.titlesize"   : 11,
    "axes.titleweight" : "bold",
    "axes.labelsize"   : 9,
    "xtick.labelsize"  : 8,
    "ytick.labelsize"  : 8,
    "legend.fontsize"  : 8,
    "figure.facecolor" : "#f8f9fa",
    "axes.facecolor"   : "#ffffff",
    "axes.edgecolor"   : "#cccccc",
    "axes.linewidth"   : 0.8,
    "grid.color"       : "#e5e5e5",
    "grid.linewidth"   : 0.6,
})

BLUE   = "#1f4e79"
ORANGE = "#ed7d31"
GREEN  = "#70ad47"
LBLUE  = "#a0b4c8"
LORG   = "#f4b183"
colors_main = [BLUE, ORANGE, GREEN]

algo_names = list(results.keys())

fig = plt.figure(figsize=(24, 22))
fig.patch.set_facecolor("#f0f4f8")

fig.suptitle(
    "Iris Flower Classification Using AI",
    fontsize=20, fontweight="bold",
    color="#1a1a2e", y=0.995
)

gs = gridspec.GridSpec(4, 3, figure=fig, hspace=0.58, wspace=0.38,
                    top=0.96, bottom=0.03, left=0.05, right=0.97)

def style_ax(ax, title):
    ax.set_title(title, pad=10, color="#1a1a2e")
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

# ROW 0 

# Elbow Curve
ax1 = fig.add_subplot(gs[0, 0])
ax1.plot(list(k_range), error_rates, "o-",
        color=BLUE, linewidth=2, markersize=5, markerfacecolor="white",
        markeredgewidth=1.5)
ax1.axvline(optimal_k, color=ORANGE, linestyle="--",
            linewidth=1.8, label=f"Optimal K = {optimal_k}")
ax1.fill_between(list(k_range), error_rates, alpha=0.08, color=BLUE)
style_ax(ax1, "Elbow Curve — Finding Optimal K")
ax1.set_xlabel("K Value"); ax1.set_ylabel("Error Rate")
ax1.legend()

# KNN Confusion Matrix
ax2 = fig.add_subplot(gs[0, 1])
disp = ConfusionMatrixDisplay(confusion_matrix=knn_cm,
                            display_labels=class_names)
disp.plot(ax=ax2, colorbar=False, cmap="Blues")
style_ax(ax2, f"KNN Confusion Matrix  (K={optimal_k})")
ax2.tick_params(axis="x", labelrotation=12)

# Algorithm Accuracy
ax3 = fig.add_subplot(gs[0, 2])
algo_accs  = [results[n]["acc"] * 100 for n in algo_names]
bar_colors = [BLUE if n == best_algo else LBLUE for n in algo_names]
bars = ax3.bar(algo_names, algo_accs, color=bar_colors,
            width=0.5, edgecolor="white", linewidth=0.8)
ax3.set_ylim(80, 102)
for bar, val in zip(bars, algo_accs):
    ax3.text(bar.get_x() + bar.get_width()/2, val + 0.4,
            f"{val:.1f}%", ha="center", fontsize=9,
            fontweight="bold", color="#1a1a2e")
style_ax(ax3, "Algorithm Accuracy Comparison")
ax3.set_ylabel("Accuracy (%)")
ax3.tick_params(axis="x", labelrotation=10)


#  ROW 1 

# F1 Score comparison
ax4 = fig.add_subplot(gs[1, 0])
algo_f1s    = [results[n]["f1"] for n in algo_names]
bar_colors2 = [ORANGE if n == best_algo else LORG for n in algo_names]
bars2 = ax4.bar(algo_names, algo_f1s, color=bar_colors2,
                width=0.5, edgecolor="white", linewidth=0.8)
ax4.set_ylim(0.85, 1.05)
for bar, val in zip(bars2, algo_f1s):
    ax4.text(bar.get_x() + bar.get_width()/2, val + 0.003,
            f"{val:.4f}", ha="center", fontsize=9,
            fontweight="bold", color="#1a1a2e")
style_ax(ax4, "Algorithm F1 Score Comparison")
ax4.set_ylabel("F1 Score (Weighted)")
ax4.tick_params(axis="x", labelrotation=10)

# CV Mean ± Std
ax5 = fig.add_subplot(gs[1, 1])
cv_means = [cv_results[n].mean() for n in algo_names]
cv_stds  = [cv_results[n].std()  for n in algo_names]
bars3 = ax5.bar(algo_names, cv_means, yerr=cv_stds,
                color=colors_main, capsize=7,
                width=0.5, edgecolor="white", alpha=0.88)
ax5.set_ylim(0.80, 1.05)
for i, (m, s) in enumerate(zip(cv_means, cv_stds)):
    ax5.text(i, m + s + 0.006, f"{m:.3f}", ha="center",
            fontsize=9, fontweight="bold", color="#1a1a2e")
style_ax(ax5, "5-Fold CV Mean F1 ± Std Dev")
ax5.set_ylabel("F1 Score")
ax5.tick_params(axis="x", labelrotation=10)

# CV Box Plot
ax6 = fig.add_subplot(gs[1, 2])
box_data = [cv_results[n] for n in algo_names]
bp = ax6.boxplot(box_data, labels=algo_names, patch_artist=True,
                medianprops=dict(color="white", linewidth=2.5),
                whiskerprops=dict(linewidth=1.2),
                capprops=dict(linewidth=1.2),
                flierprops=dict(marker="o", markersize=5))
for patch, color in zip(bp["boxes"], colors_main):
    patch.set_facecolor(color)
    patch.set_alpha(0.85)
style_ax(ax6, "CV Score Distribution")
ax6.set_ylabel("F1 Score")
ax6.tick_params(axis="x", labelrotation=10)


# ROW 2

# Decision Tree Confusion Matrix
ax7 = fig.add_subplot(gs[2, 0])
cm_dt = confusion_matrix(y_test, results["Decision Tree"]["preds"])
ConfusionMatrixDisplay(confusion_matrix=cm_dt,
                    display_labels=class_names).plot(
    ax=ax7, colorbar=False, cmap="Oranges")
style_ax(ax7, "Decision Tree Confusion Matrix")
ax7.tick_params(axis="x", labelrotation=12)

# Logistic Regression Confusion Matrix
ax8 = fig.add_subplot(gs[2, 1])
cm_lr = confusion_matrix(y_test, results["Logistic Regression"]["preds"])
ConfusionMatrixDisplay(confusion_matrix=cm_lr,
                    display_labels=class_names).plot(
    ax=ax8, colorbar=False, cmap="Greens")
style_ax(ax8, "Logistic Regression Confusion Matrix")
ax8.tick_params(axis="x", labelrotation=12)

# Per-class F1 all algorithms
ax9 = fig.add_subplot(gs[2, 2])
x_pos = np.arange(len(class_names))
width = 0.25
for i, (name, color) in enumerate(zip(algo_names, colors_main)):
    rep = classification_report(
        y_test, results[name]["preds"],
        target_names=class_names, output_dict=True)
    f1_vals = [rep[c]["f1-score"] for c in class_names]
    ax9.bar(x_pos + i * width, f1_vals, width,
            label=name, color=color, alpha=0.85,
            edgecolor="white", linewidth=0.8)
ax9.set_ylim(0, 1.15)
ax9.set_xticks(x_pos + width)
ax9.set_xticklabels(class_names)
ax9.set_ylabel("F1 Score")
ax9.legend()
style_ax(ax9, "Per-Class F1 — All Algorithms")


# ROW 3

# Scatter with custom flowers
ax10 = fig.add_subplot(gs[3, 0])
for i, name in enumerate(class_names):
    mask = y == i
    ax10.scatter(X[mask, 2], X[mask, 3],
                label=name, color=colors_main[i],
                alpha=0.60, s=45, edgecolors="none")
star_colors = ["#e63946", "#457b9d", "#2d6a4f"]
star_labels = ["Custom 1 → Setosa",
            "Custom 2 → Versicolor",
            "Custom 3 → Virginica"]
for i, flower in enumerate(custom_flowers):
    ax10.scatter(flower[2], flower[3], marker="*", s=320,
                color=star_colors[i], edgecolors="white",
                linewidths=0.8, zorder=5, label=star_labels[i])
style_ax(ax10, "Petal Length vs Width  +  Custom Flowers *")
ax10.set_xlabel("Petal Length (cm)")
ax10.set_ylabel("Petal Width (cm)")
ax10.legend(loc="upper left", fontsize=7)

# Custom Prediction Results box
ax11 = fig.add_subplot(gs[3, 1])
ax11.axis("off")
pred_lines = [
    "  CUSTOM PREDICTION RESULTS",
    "  " + "─" * 36,
    f"  {'Flower':<9} {'Measurements':<20} {'Result'}",
    "  " + "─" * 36,
]
for i, (flower, scaled) in enumerate(zip(custom_flowers, custom_scaled)):
    pred_class = knn_model.predict([scaled])[0]
    proba      = knn_model.predict_proba([scaled])[0]
    conf       = proba[pred_class] * 100
    species    = class_names[pred_class]
    meas       = f"[{flower[0]},{flower[1]},{flower[2]},{flower[3]}]"
    pred_lines.append(f"  Flower {i+1}   {meas}")
    pred_lines.append(f"  {'':>9} → {species}  ({conf:.0f}% conf)")
    pred_lines.append("  " + "─" * 36)
pred_lines += ["", "  SL=SepalLen  SW=SepalWid",
            "  PL=PetalLen  PW=PetalWid"]

ax11.text(0.04, 0.97, "\n".join(pred_lines),
        transform=ax11.transAxes,
        fontsize=9.5, verticalalignment="top",
        fontfamily="monospace",
        bbox=dict(boxstyle="round,pad=0.7",
                    facecolor="#fff8e7",
                    edgecolor="#f0c040",
                    linewidth=1.5, alpha=0.95))

# Final Summary box
ax12 = fig.add_subplot(gs[3, 2])
ax12.axis("off")
best_cv      = max(cv_results, key=lambda n: cv_results[n].mean())
best_cv_mean = cv_results[best_cv].mean()

summary_lines = [
    "  FINAL SUMMARY",
    "  " + "─" * 32,
    "  Dataset    : Iris  (150 samples)",
    "  Split      : 80% train / 20% test",
    "  Scaling    : StandardScaler",
    "  " + "─" * 32,
]
for name in algo_names:
    summary_lines.append(f"  {name}")
    summary_lines.append(
        f"    Acc = {results[name]['acc']*100:.1f}%   "
        f"F1 = {results[name]['f1']:.4f}"
    )
summary_lines += [
    "  " + "─" * 32,
    f"  Best Model  : {best_algo}",
    f"  Best CV F1  : {best_cv_mean:.4f}",
    f"  KNN Acc     : {knn_acc*100:.2f}%",
    f"  KNN F1      : {knn_f1:.4f}",
]

ax12.text(0.04, 0.97, "\n".join(summary_lines),
        transform=ax12.transAxes,
        fontsize=9.5, verticalalignment="top",
        fontfamily="monospace",
        bbox=dict(boxstyle="round,pad=0.7",
                    facecolor="#eaf4fb",
                    edgecolor="#5b9bd5",
                    linewidth=1.5, alpha=0.95))

plt.savefig("dashboard.png", dpi=150, bbox_inches="tight")
plt.close()
print("  Dashboard saved -> dashboard.png")


# Final Console Summary
print("\n" + "=" * 65)
print("  ALL STEPS COMPLETE — SUMMARY:")
print("  ┌─────────────────────────────────────────────────┐")
print(f"  │  KNN Accuracy        : {knn_acc*100:.2f}%                   │")
print(f"  │  KNN F1 Score        : {knn_f1:.4f}                   │")
print(f"  │  Best Algorithm      : {best_algo:<25}│")
print(f"  │  Best CV F1 (5-Fold) : {best_cv_mean:.4f}                   │")
print("  └─────────────────────────────────────────────────┘")
print("=" * 65)
