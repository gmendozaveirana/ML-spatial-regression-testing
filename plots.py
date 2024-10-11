import matplotlib.pyplot as plt
import numpy as np

def threedgraph(y_, x_, z_, Long, Lat, regression, mode, title, long_tran, lat_tran):

    plt.rcParams["figure.figsize"] = (6,4)
    plt.rcParams["figure.dpi"] = 150
    fig = plt.figure()
    ax = fig.add_subplot(projection = "3d")
    ax.scatter(y_, x_, -z_, c = "navy")
    ax.tick_params(axis='y', labelsize=6)
    ax.tick_params(axis='x', labelsize=6)
    ax.set_xlabel("Longitude", fontweight='bold', fontsize=12)
    ax.set_ylabel("Latitude", fontweight='bold', fontsize=12)
    ax.set_zlabel("MASL", fontweight='bold', fontsize=14)
    ax.set_title(title, fontweight='bold', fontsize=16)

    if mode == "simple":
        ax.scatter(Long, Lat, regression, c = "darkorange", s = 0.5)
        
    elif mode == "transect": 
        ax.scatter(long_tran, lat_tran, regression, c = "red", s = 0.5)
    
    elif mode == "cloud": 
        ax.scatter(y_, x_, regression, c = "darkorange") 


def plot_svm_results(C_values, Gamma_values, EXPS_TEST, EXPS_TRAIN, EXPS_CV, EXPMSE_TEST, EXPMSE_TRAIN):
    """
    Creates scatter plots for SVR test, train scores, cross-validation scores, and MSE.
    """
    # Prepare data for visualization
    C_grid, Gamma_grid = np.meshgrid(C_values, Gamma_values, indexing='ij')
    
    # Create plots for SVR scores
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, sharex=True, figsize=(5, 10))

    # Scatter plots for scores
    ax3.scatter(C_grid, Gamma_grid, s=(EXPS_CV + 1) ** 5, c="cyan", label="CV Score")
    ax1.scatter(C_grid, Gamma_grid, s=(EXPS_TEST + 0.3) ** 15, c="red", label="Test Score")
    ax2.scatter(C_grid, Gamma_grid, s=(EXPS_TRAIN + 0.3) ** 12, c="blue", label="Train Score")

    # Adjust plot scales and labels
    for ax in [ax1, ax2, ax3]:
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.set_xlim(20, 800000)
        ax.set_ylim(0.00001, 31)
        ax.tick_params(labelsize=12)

    ax1.set_ylabel("Gamma", fontweight='bold', fontsize=16)
    ax2.set_ylabel("Gamma", fontweight='bold', fontsize=16)
    ax3.set_ylabel("Gamma", fontweight='bold', fontsize=16)
    ax3.set_xlabel("C", fontweight='bold', fontsize=16)
    ax1.set_title("SVR Test Score", fontweight='bold', fontsize=20)
    ax2.set_title("SVR Train Score", fontweight='bold', fontsize=20)
    ax3.set_title("SVR CV Score", fontweight='bold', fontsize=20)

    # Save the plot
    plt.savefig("MendozaVeirana_et_al(2021)_SVMscore_figure.png", dpi=300)
    plt.close(fig)

    # MSE scatter plots
    fig2, (ax4, ax5) = plt.subplots(2, 1, sharex=True, figsize=(5, 7))

    ax4.scatter(C_grid, Gamma_grid, s=(EXPMSE_TEST) ** 0.4, c="red", label="Test MSE")
    ax5.scatter(C_grid, Gamma_grid, s=(EXPMSE_TRAIN) ** 0.4, c="blue", label="Train MSE")

    for ax in [ax4, ax5]:
        ax.set_xscale('log')
        ax.set_yscale('log')
        ax.set_xlim(20, 800000)
        ax.set_ylim(0.00001, 31)
        ax.tick_params(labelsize=12)

    ax4.set_ylabel("Gamma", fontweight='bold', fontsize=16)
    ax5.set_ylabel("Gamma", fontweight='bold', fontsize=16)
    ax4.set_title("SVR Test MSE", fontweight='bold', fontsize=20)
    ax5.set_title("SVR Train MSE", fontweight='bold', fontsize=20)

    # Save the plot
    plt.savefig("output/MendozaVeirana_et_al(2021)_SVMmse_figure.png", dpi=300)
    plt.close(fig2)


