from typing import Dict

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def plot_learning_curves(results: Dict):
    """
    Строит графики кривых обучения по результатам, полученным из run_gradient_descent_experiments.
    Каждый график соответствует одному значению порога остановки (threshold),
    и на нем отображены кривые для различных значений learning rate.
    """
    # Устанавливаем стиль seaborn для более эстетичных графиков
    sns.set(style="whitegrid", context="talk", palette="tab10")

    # Получаем список всех порогов и learning rate из результатов
    threshold_list = list(results.keys())
    lr_list = list(next(iter(results.values())).keys())

    # Задаем количество столбцов и строк в сетке подграфиков
    cols = 2
    rows = len(threshold_list) // 2 + len(threshold_list) % 2

    # Создаем сетку графиков
    fig, axes = plt.subplots(nrows=rows, ncols=cols, figsize=(18, 6 * rows), sharey=True)

    # Преобразуем axes в 2D массив на случай, если он одномерный
    axes = np.atleast_2d(axes)

    # Перебираем все подграфики, соответствующие разным threshold
    for idx, t in enumerate(threshold_list):
        row_idx = idx // cols
        col_idx = idx % cols
        ax = axes[row_idx][col_idx]

        # Строим кривые обучения для каждого learning rate
        for lr in lr_list:
            loss_data = results[t][lr]["losses"]
            final_loss = results[t][lr]["final_loss"]

            # Строим линию кривой обучения
            sns.lineplot(
                x=list(loss_data.keys()),
                y=list(loss_data.values()),
                ax=ax,
                label=f"LR: {lr:.0e}, Q: {final_loss:.4f}",
            )

        # Настройки подграфика: заголовок, подписи, легенда, сетка
        ax.set_title(f"Threshold = {t:.0e}", fontsize=20)
        ax.set_ylabel("MSE", fontsize=14)
        ax.set_xlabel("Step Number", fontsize=14)
        ax.legend(fontsize=10)
        ax.grid(True)

    # Заголовок всей фигуры
    fig.suptitle("Learning Curves for Gradient Descent (MSE)", fontsize=24, y=1.02)

    # Автоматическая компоновка графиков
    fig.tight_layout()

    # Отображение графика
    plt.show()
