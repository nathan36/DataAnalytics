import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import re
import numpy as np

# Seaborn plots
sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize":(8,4)})
# R style
# mpl.rcParams['axes.labelsize'] = 9
# mpl.rcParams['xtick.labelsize'] = 9
# mpl.rcParams['ytick.labelsize'] = 9
# mpl.rcParams['legend.labelsize'] = 7
# mpl.rcParams['font.serif'] = ['Computer Modern Roman']
# mpl.rcParams['text.usetex'] = False
# mpl.rcParams['figure.figsize'] = 20, 10

def plot_tweets_per_category(category, title, x_title, y_title, top_n=5):
    """
    :param category: Data field
    :param title: Title of the plot
    :param x_title: List of the items in x
    :param y_title: Title of the variable plotted
    :return: a plot displayed in console
    """
    tweets_by_cat = category.value_counts()
    fig, ax = plt.subplots()
    ax.tick_params(axis='x')
    ax.tick_params(axis='y')
    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)
    ax.set_title(title)
    tweets_by_cat[:top_n].plot(ax=ax, kind='bar')
    plt.show()

def plot_distribution(category, title, x_title, y_title):
    """
    :param category: Aggregated field
    :param title: Title of the plot
    :param x_title: List of the items in x
    :param y_title: Title of the variable plotted
    :return: a distribution plot displayed in console
    """
    fig, ax = plt.subplots()
    ax.tick_params(axis='x')
    ax.tick_params(axis='y')
    ax.set_xlabel(x_title)
    ax.set_ylabel(y_title)
    ax.set_title(title)
    sns.distplot(category.values, rug=True, hist=True);
    plt.show()

def draw_wordcloud(data, mask_img_path):
    """
    :param data: A txt file with one line of string
    :param mask_img_path: Image used for masking
    :return: a word cloud
    """
    mask = np.array(Image.open(mask_img_path))
    wc = WordCloud(background_color="white", stopwords=STOPWORDS, mask=mask)
    wc.generate(data)
    plt.imshow(wc)
    plt.axis("off")
    plt.show()

def word_search(word, text):
    word = word.lower()
    text = text.lower()
    match = re.search(word, text)
    if match:
        return True
    else:
        return False