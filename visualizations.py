import matplotlib.pyplot as plt

def create_scatter_plot():
    plt.scatter([1,2,3,4,5], [4,3,2,1])
    filename = "fig.png"

    plt.savefig(filename)
    print(f"Saved file as {filename}")

    plt.close()
    #plt.show()

def create_bar_plot():
    plt.bar(['A', 'B', 'C', 'D'], [4,3,4,5])
    plt.show()
    plt.close()
    

