import os

import numpy as np
import matplotlib.pyplot as plt

if __name__ == '__main__':
    directory = "170/loopfinal/loopfinal"
    accs = {}
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        fold = int(os.path.basename(f)[:-4])
        file = open(f, 'r')

        accs[fold] = []
        for line in file:
            accs[fold].append(float(line.replace("\n", "").split(", ")[1].split(" ")[1]))

    average_accross_each_fold = []
    overal_average_over_all_epochs_folds = 0
    overal_best_average_over_all_epoch_folds = 0
    overal_best_average_over_all_epochs = []
    for acc in accs:

        average_accross_each_fold.append(accs.get(acc)[-1])
        overal_average_over_all_epochs_folds += np.mean(accs.get(acc))
        overal_best_average_over_all_epoch_folds += np.min(accs.get(acc))
        overal_best_average_over_all_epochs.append(np.min(accs.get(acc)))


    plt.plot(average_accross_each_fold)
    plt.title("(Scaled)Average Folds versus Degrees(Batch Size 170)")
    plt.xlabel("Folds")
    plt.ylabel("Degrees")
    plt.show()

    plt.plot(overal_best_average_over_all_epochs)
    plt.title("(Scaled)Best Folds versus Degrees(Batch Size 170)")
    plt.xlabel("Folds")
    plt.ylabel("Degrees")
    plt.show()

    print()
    print("170 (Scaled)best_avg_over_all_epochs", overal_best_average_over_all_epoch_folds/14)
    print("170 (Scaled)overal_average_over_all_epochs_folds", overal_average_over_all_epochs_folds/14)
    print("170 (Scaled)standard deviation for best_avg", np.std(overal_best_average_over_all_epochs))
    print("170 (Scaled)standard deviation for overal_average_over_all_epochs_folds", np.std(average_accross_each_fold))
    print()

    directory = "170/loopfinal_nonscale/loopfinal_nonscale"
    accs = {}
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        fold = int(os.path.basename(f)[:-4])
        file = open(f, 'r')

        accs[fold] = []
        for line in file:
            accs[fold].append(float(line.replace("\n", "").split(", ")[1].split(" ")[1]))

    average_accross_each_fold = []
    overal_average_over_all_epochs_folds = 0
    overal_best_average_over_all_epoch_folds = 0
    overal_best_average_over_all_epochs = []
    for acc in accs:
        average_accross_each_fold.append(np.mean(accs.get(acc)))
        overal_average_over_all_epochs_folds += np.mean(accs.get(acc))
        overal_best_average_over_all_epoch_folds += np.min(accs.get(acc))
        overal_best_average_over_all_epochs.append(np.min(accs.get(acc)))

    plt.plot(average_accross_each_fold)
    plt.title("(NotScaled)Average Folds versus Degrees(Batch Size 170)")
    plt.xlabel("Folds")
    plt.ylabel("Degrees")
    plt.show()

    plt.plot(overal_best_average_over_all_epochs)
    plt.title("(NotScaled)Best Folds versus Degrees(Batch Size 170)")
    plt.xlabel("Folds")
    plt.ylabel("Degrees")
    plt.show()

    print()
    print("170 (NotScaled)best_avg_over_all_epochs", overal_best_average_over_all_epoch_folds / 14)
    print("170 (NotScaled)overal_average_over_all_epochs_folds", overal_average_over_all_epochs_folds / 14)
    print("170 (NotScaled)standard deviation for best_avg", np.std(overal_best_average_over_all_epochs))
    print("170 (NotScaled)standard deviation for overal_average_over_all_epochs_folds", np.std(average_accross_each_fold))
    print()


    directory = "110/loopfinal/loopfinal"
    accs = {}
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        fold = int(os.path.basename(f)[:-4])
        file = open(f, 'r')

        accs[fold] = []
        for line in file:
            accs[fold].append(float(line.replace("\n", "").split(", ")[1].split(" ")[1]))

    average_accross_each_fold = []
    overal_average_over_all_epochs_folds = 0
    overal_best_average_over_all_epoch_folds = 0
    overal_best_average_over_all_epochs = []
    for acc in accs:
        average_accross_each_fold.append(np.mean(accs.get(acc)))
        overal_average_over_all_epochs_folds += np.mean(accs.get(acc))
        overal_best_average_over_all_epoch_folds += np.min(accs.get(acc))
        overal_best_average_over_all_epochs.append(np.min(accs.get(acc)))


    plt.plot(average_accross_each_fold)
    plt.title("(Scaled)Average Folds versus Degrees(Batch Size 170)")
    plt.xlabel("Folds")
    plt.ylabel("Degrees")
    plt.show()

    plt.plot(overal_best_average_over_all_epochs)
    plt.title("(Scaled)Best Folds versus Degrees(Batch Size 170)")
    plt.xlabel("Folds")
    plt.ylabel("Degrees")
    plt.show()
    print()
    print("110 (Scaled)best_avg_over_all_epochs", overal_best_average_over_all_epoch_folds/14)
    print("110 (Scaled)overal_average_over_all_epochs_folds", overal_average_over_all_epochs_folds/14)
    print("110 (Scaled)standard deviation for best_avg", np.std(overal_best_average_over_all_epochs))
    print("110 (Scaled)standard deviation for overal_average_over_all_epochs_folds", np.std(average_accross_each_fold))
    print()
    directory = "110/loopfinal_nonscale"
    accs = {}
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        fold = int(os.path.basename(f)[:-4])
        file = open(f, 'r')

        accs[fold] = []
        for line in file:
            accs[fold].append(float(line.replace("\n", "").split(", ")[1].split(" ")[1]))

    average_accross_each_fold = []
    overal_average_over_all_epochs_folds = 0
    overal_best_average_over_all_epoch_folds = 0
    overal_best_average_over_all_epochs = []
    for acc in accs:
        average_accross_each_fold.append(np.mean(accs.get(acc)))
        overal_average_over_all_epochs_folds += np.mean(accs.get(acc))
        overal_best_average_over_all_epoch_folds += np.min(accs.get(acc))
        overal_best_average_over_all_epochs.append(np.min(accs.get(acc)))

    plt.plot(average_accross_each_fold)
    plt.title("(NotScaled)Average Folds versus Degrees(Batch Size 110)")
    plt.xlabel("Folds")
    plt.ylabel("Degrees")
    plt.show()

    plt.plot(overal_best_average_over_all_epochs)
    plt.title("(NotScaled)Best Folds versus Degrees(Batch Size 110)")
    plt.xlabel("Folds")
    plt.ylabel("Degrees")
    plt.show()

    print()
    print("110 (NotScaled)best_avg_over_all_epochs", overal_best_average_over_all_epoch_folds / 14)
    print("110 (NotScaled)overal_average_over_all_epochs_folds", overal_average_over_all_epochs_folds / 14)
    print("110 (NotScaled)standard deviation for best_avg", np.std(overal_best_average_over_all_epochs))
    print("110 (NotScaled)standard deviation for overal_average_over_all_epochs_folds", np.std(average_accross_each_fold))
