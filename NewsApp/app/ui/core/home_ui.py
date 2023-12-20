from tkinter import *
import customtkinter
from api.news_api import NewsApi
import webbrowser


class HomeUI(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.news_api = NewsApi()
        self.master.grid_columnconfigure(1, weight=1)
        self.master.grid_columnconfigure(2, weight=1)
        self.master.grid_columnconfigure(3, weight=1)

        # label data início
        self.fromDateLabel = customtkinter.CTkLabel(master, text='De')
        self.fromDateLabel.grid(row=2, column=0, padx=5, pady=10)

        # data início
        self.fromDateDay = customtkinter.CTkEntry(
            master, placeholder_text="dd")
        self.fromDateMonth = customtkinter.CTkEntry(
            master, placeholder_text="mm")
        self.fromDateYear = customtkinter.CTkEntry(
            master, placeholder_text="yyyy")

        self.fromDateDay.grid(row=2, column=1, padx=5,
                              pady=10, columnspan=1, sticky="ew")
        self.fromDateMonth.grid(row=2, column=2, padx=5,
                                pady=10, columnspan=1, sticky="ew")
        self.fromDateYear.grid(row=2, column=3, padx=5,
                               pady=10, columnspan=1, sticky="ew")

        # label data fim
        self.toDateLabel = customtkinter.CTkLabel(master, text='a')
        self.toDateLabel.grid(row=3, column=0, padx=5, pady=10)

        # data fim
        self.toDateDay = customtkinter.CTkEntry(master, placeholder_text="dd")
        self.toDateMonth = customtkinter.CTkEntry(
            master, placeholder_text="mm")
        self.toDateYear = customtkinter.CTkEntry(
            master, placeholder_text="yyyy")

        self.toDateDay.grid(row=3, column=1, padx=5,
                            pady=10, columnspan=1, sticky="ew")
        self.toDateMonth.grid(row=3, column=2, padx=5,
                              pady=10, columnspan=1, sticky="ew")
        self.toDateYear.grid(row=3, column=3, padx=5,
                             pady=10, columnspan=1, sticky="ew")

        # label tópico
        self.topicLabel = customtkinter.CTkLabel(master, text='Tópico')
        self.topicLabel.grid(row=4, column=0, padx=5, pady=10)

        # tópico da notícia
        self.topic = customtkinter.CTkEntry(
            master, placeholder_text="Tópico da notícia")
        self.topic.grid(row=4, column=1, padx=5, pady=10,
                        columnspan=1, sticky="ew")

        # label língua
        self.languageLabel = customtkinter.CTkLabel(master, text='Língua')
        self.languageLabel.grid(row=4, column=2, padx=5, pady=10)

        # língua (pt, en, ar, etc)
        self.language = customtkinter.CTkEntry(
            master, placeholder_text="Língua (pt, en, ar, etc)")
        self.language.grid(row=4, column=3, padx=5, pady=10,
                           columnspan=1, sticky="ew")

        # botão de pesquisa
        self.searchButton = customtkinter.CTkButton(
            master, text="Buscar", command=self.search)
        self.searchButton.grid(row=5, columnspan=4,
                               padx=5, pady=10, sticky="ew")

        # notícias
        self.textbox = customtkinter.CTkTextbox(
            master, corner_radius=5, border_spacing=10)
        self.textbox.grid(row=6, columnspan=4, sticky="nsew")

        self.load_news()

    def cleanForm(self):
        self.fromDateDay.delete(0, END)
        self.fromDateMonth.delete(0, END)
        self.fromDateYear.delete(0, END)
        self.toDateDay.delete(0, END)
        self.toDateMonth.delete(0, END)
        self.toDateYear.delete(0, END)
        self.language.delete(0, END)
        self.topic.delete(0, END)

    def load_news(self):
        # Limpar a lista de notícias antes de atualizar
        self.textbox.configure(state="normal")
        self.textbox.delete("1.0", "end")

        for article in self.news_api.articles:
            title = article.get('title', 'N/A')
            link = article.get('url', '#')

            # Adicione a notícia ao Text
            news_text = f"{title}\n{link}\n\n"
            self.textbox.insert("end", news_text)

        self.textbox.configure(state="disabled")

    def search(self):
        fromDate = f"{self.fromDateYear.get()}-{self.fromDateMonth.get()}-{self.fromDateDay.get()}"
        toDate = f"{self.toDateYear.get()}-{self.toDateYear.get()}-{self.toDateYear.get()}"
        topic = self.topic.get()
        language = self.language.get()

        self.news_api.get_specific_news(
            topic=topic, fromDate=fromDate, toDate=toDate, language=language)

        self.load_news()
        self.cleanForm()
