'''This projeckt by Mostafa Hazem , this project is mhd about chatbot and this project by python.'''

from gtts import gTTS

import math 

import random

import speech_recognition as sr 

import threading

import tkinter as tk

import pyttsx3

from tkinter import ttk, messagebox

from tkinter import Entry, Button,  Label 

import os

from tkinter import Canvas

import pygame

from time import strftime, localtime

import os

import datetime

import json


button_width = 15

button_padding = 10

button_distance = 5

now = datetime.datetime.now()

new1 = now 

now3 = new1.strftime('%H:%M')

space = "\t\t\t\t\t  "

notes = []

new_note = ""

mhd9 = "MHD-CHATBOT : "

user_name = "YOU"

def mhd(question):
    if "who" in question.lower() and "programming" in question.lower():
     
      if "mostafa hazem" in user_name.lower():
         response = "I am MHD, a chatbot created by You." 
      else:
         response = "I am MHD, a chatbot created by Mostafa Hazem Jibreel."

    elif "you" in question.lower() and "name" in question.lower():
      response = "My name is MHD."

    elif "hello" in question.lower() or "hi" in question.lower() or "hey" in question.lower() or "welcome" in question.lower() :
      response = question.lower()+ ", what can I do for you?"
    

    elif "how" in question.lower() and "are" in question.lower() and "you" in question.lower():
      response = "I am find, thank you for asking."

    elif "capital" in question.lower() and "france" in question.lower():
      response = "The capital of France is Paris."

    elif "country" in question.lower() and "large" in question.lower():
      response = "The largest country in the world by land area is Russia."

    elif "river" in question.lower() and "long" in question.lower():
      response = "The Nile River is considered the longest river in the world."

    elif "old" in question.lower() and "university" in question.lower():
      response = "The oldest university in the world that is still in operation is the University of Bologna in Italy."

    elif "fast" in question.lower() and "animal" and "world" in question.lower():
      response = "The cheetah is the fastest land animal in the world."

    elif "large" in question.lower() and "ocean" in question.lower():
      response = "The Pacific Ocean is the largest ocean in the world."

    elif "tall" in question.lower() and "mountain" in question.lower():
      response = "Mount Everest is the tallest mountain in the world."

    elif "longe" in question.lower() and "bridge" in question.lower():
      response = "The Danyang–Kunshan Grand Bridge in China is the longest bridge in the world."

    elif "big" in question.lower() and "desert" in question.lower():
      response = "The Sahara Desert is the largest hot desert in the world."

    elif "most" in question.lower() and "spoke" in question.lower() and "language" in question.lower():
      response = "The most spoken language in the world is Mandarin Chinese."

    elif "old" in question.lower() and "civilization" in question.lower():
      response = "The Mesopotamian civilization is one of the oldest civilizations in the world."

    elif "deep" in question.lower() and "ocean" in question.lower():
      response = "The deepest part of the ocean is the Mariana Trench in the Pacific Ocean."

    elif "large" in question.lower() and "continent" in question.lower():
      response = "Asia is the largest continent in the world."

    elif "hot" in question.lower() and "place" in question.lower():
      response = "The hottest place on Earth is Furnace Creek Ranch in Death Valley, California, USA."

    elif "cold" in question.lower() and "place" in question.lower():
      response = "The coldest inhabited place on Earth is Oymyakon, Russia."

    elif "fast" in question.lower() and "bird" in question.lower():
      response = "The peregrine falcon is the fastest bird in the world."

    elif "large" in question.lower() and "mammal" in question.lower():
      response = "The blue whale is the largest mammal in the world."

    elif "tall" in question.lower() and "tree" in question.lower():
      response = "The tallest tree in the world is Hyperion, a coast redwood (Sequoia sempervirens) in California, USA."

    elif "deep" in question.lower() and "lake" in question.lower():
      response = "The deepest lake in the world is Lake Baikal in Russia."

    elif "most" in question.lower() and "popul" in question.lower() and "country" in question.lower():
      response = "The most populous country in the world is China."

    elif "large" in question.lower() and "volcano" in question.lower():
      response = "Mauna Loa in Hawaii is the largest volcano on Earth by volume and area covered."

    elif "big" in question.lower() and "island" in question.lower():
      response = "Greenland is the largest island in the world by area."

    elif "high" in question.lower() and "waterfall" in question.lower():
      response = "Angel Falls in Venezuela is the highest waterfall in the world."

    elif "fast" in question.lower() and "land" in question.lower() and "animal" in question.lower():
      response = "The cheetah is the fastest land animal in the world."

    elif "longe" in question.lower() and "coastline" in question.lower():
      response = "Canada has the longest coastline in the world."

    elif "most" in question.lower() and "visited" in question.lower() and "city" in question.lower():
      response = "Bangkok, Thailand, is one of the most visited cities in the world."

    elif "large" in question.lower() and "airport" in question.lower():
      response = "King Fahd International Airport in Dammam, Saudi Arabia, is the largest airport in the world by area."

    elif "bus" in question.lower() and "airport" in question.lower():
      response = "Hartsfield–Jackson Atlanta International Airport in the United States is one of the busiest airports in the world."

    elif "longe" in question.lower() and "beach" in question.lower():
      response = "Praia do Cassino Beach in Brazil is considered the longest beach in the world."

    elif "high" in question.lower() and "peak" in question.lower():
      response = "Mount Everest is the highest peak in the world above sea level."

    elif "big" in question.lower() and "zoo" in question.lower():
      response = "The San Diego Zoo in California, USA, is one of the largest zoos in the world."

    elif "large" in question.lower() and "dam" in question.lower():
      response = "The Three Gorges Dam in China is the largest dam in the world by electricity production."

    elif "most" in question.lower() and "famous" in question.lower() and "painting" in question.lower():
      response = "The Mona Lisa, painted by Leonardo da Vinci, is one of the most famous paintings in the world."

    elif "old" in question.lower() and "city" in question.lower():
      response = "Jericho in the West Bank is one of the oldest continuously inhabited cities in the world."

    elif "big" in question.lower() and "lake" in question.lower():
      response = "Lake Superior, one of the Great Lakes in North America, is the largest freshwater lake by surface area in the world."

    elif "first" in question.lower() and "man" in question.lower() and "moon" in question.lower():
      response = "Neil Armstrong was the first man to walk on the moon during the Apollo 11 mission in 1969."

    elif "large" in question.lower() and "library" in question.lower():
      response = "The Library of Congress in Washington, D.C., USA, is the largest library in the world."

    elif "expensive" in question.lower() and "painting" in question.lower():
      response = "Salvator Mundi by Leonardo da Vinci holds the record for the most expensive painting ever sold."

    elif "fast" in question.lower() and "land" in question.lower() and "vehicle" in question.lower():
      response = "The ThrustSSC holds the land speed record of 763.035 mph (1,227.986 km/h)."

    elif "big" in question.lower() and "pyramid" in question.lower():
      response = "The Great Pyramid of Giza in Egypt is the largest pyramid in the world."

    elif "popula" in question.lower() and "city" in question.lower():
      response = "Tokyo, Japan, is one of the most populated cities in the world."

    elif "first" in question.lower() and "computer" in question.lower():
      response = "Ada Lovelace, an English mathematician, is considered the world's first computer programmer."

    elif "large" in question.lower() and "art" in question.lower() and "museum" in question.lower():
      response = "The Louvre in Paris, France, is the largest art museum in the world."

    elif "deadly" in question.lower() and "disease" in question.lower():
      response = "Malaria is considered one of the most deadly diseases in human history."
    elif "fast" in question.lower() and "plant" in question.lower():
      response = "Bamboo is known as the fastest-growing plant in the world."

    elif "first" in question.lower() and "space" in question.lower():
      response = "Yuri Gagarin was the first human to journey into space on April 12, 1961."

    elif "old" in question.lower() and "writ" in question.lower() and "language" in question.lower():
      response = "Sumerian is one of the oldest known written languages, originating in Mesopotamia around 3500 BCE."

    elif "longe" in question.lower() and "railway" in question.lower():
      response = "The Trans-Siberian Railway in Russia is the longest railway in the world, spanning over 9,000 kilometers."

    elif "expensive" in question.lower() and "metal" in question.lower():
      response = "Rhodium is considered the most expensive metal, valued even higher than gold or platinum."

    elif "high" in question.lower() and "paid" in question.lower() and "athlete" in question.lower():
      response = "Floyd Mayweather Jr. is one of the highest-paid athletes in history."

    elif "calculat" in question.lower() :


       def press_key(key):
           current = entry.get()
           if key == "^":
               entry.insert(tk.END, "**")
           elif key == "√":
               open_root_window()
           elif key == "delete":
               delete_last_char()
           else:
               entry.delete(0, tk.END)
               entry.insert(tk.END, current + key)

       def calculate():
           try:
               result = eval(entry.get())
               entry.delete(0, tk.END)
               entry.insert(tk.END, str(result))
           except Exception as e:
               entry.delete(0, tk.END)
               entry.insert(tk.END, "Error")

       def clear():
           entry.delete(0, tk.END)

       def delete_last_char():
           entry.delete(len(entry.get()) - 1)

       def open_root_window():
           root_window = tk.Toplevel(root)
           root_window.title("Calculate Square Root")
           root_window.geometry("300x250")
           root_window.configure(bg="#f0f0f0")

           label = tk.Label(root_window, text="Enter a number and the type of root:", font=('Arial', 12))
           label.pack(pady=5)

           number_label = tk.Label(root_window, text="Number:", font=('Arial', 12))
           number_label.pack(pady=5)
           number_entry = tk.Entry(root_window, font=('Arial', 12))
           number_entry.pack(pady=5)

           type_label = tk.Label(root_window, text="Root Type :", font=('Arial', 12))
           type_label.pack(pady=5)
           type_entry = tk.Entry(root_window, font=('Arial', 12))
           type_entry.pack(pady=5)

           calculate_button = tk.Button(root_window, text="Calculate", font=('Arial', 12),
                                        command=lambda: calculate_root(float(number_entry.get()), int(type_entry.get()), root_window))
           calculate_button.pack(pady=5)

       def calculate_root(number, root_type, window):
           result = number ** (1 / root_type)
           result_label.config(text=f"Root = {result}")
           window.destroy()

       def open_shape_window():
           shape_window = tk.Toplevel(root)
           shape_window.title("Calculate Area and Perimeter")
           shape_window.geometry("300x200")
           shape_window.configure(bg="#f0f0f0")

           label = tk.Label(shape_window, text="Please select a shape:", font=('Arial', 12))
           label.pack(pady=5)

           square_button = tk.Button(shape_window, text="Square", font=('Arial', 12),
                                     command=lambda: open_dimension_window("Square", shape_window))
           square_button.pack(pady=5)

           rectangle_button = tk.Button(shape_window, text="Rectangle", font=('Arial', 12),
                                        command=lambda: open_dimension_window("Rectangle", shape_window))
           rectangle_button.pack(pady=5)

           circle_button = tk.Button(shape_window, text="Circle", font=('Arial', 12),
                                     command=lambda: open_dimension_window("Circle", shape_window))
           circle_button.pack(pady=5)

           triangle_button = tk.Button(shape_window, text="Triangle", font=('Arial', 12),
                                       command=lambda: open_dimension_window("Triangle", shape_window))
           triangle_button.pack(pady=5)

       def open_dimension_window(shape, parent):
           dimension_window = tk.Toplevel(parent)
           dimension_window.title("Enter Dimensions")
           dimension_window.geometry("300x300")
           dimension_window.configure(bg="#f0f0f0")

           label = tk.Label(dimension_window, text=f"Please enter the dimensions \n of the {shape}:", font=('Arial', 12))
           label.pack(pady=5)

           if shape == "Square":
               side_label = tk.Label(dimension_window, text="Side length:", font=('Arial', 12))
               side_label.pack(pady=5)
               side_entry = tk.Entry(dimension_window, font=('Arial', 12))
               side_entry.pack(pady=5)
               calculate_button = tk.Button(dimension_window, text="Calculate", font=('Arial', 12),
                                            command=lambda: calculate_square_area_perimeter(float(side_entry.get()), dimension_window))
               calculate_button.pack(pady=5)
           elif shape == "Rectangle":
               length_label = tk.Label(dimension_window, text="Length:", font=('Arial', 12))
               length_label.pack(pady=5)
               length_entry = tk.Entry(dimension_window, font=('Arial', 12))
               length_entry.pack(pady=5)
               width_label = tk.Label(dimension_window, text="Width:", font=('Arial', 12))
               width_label.pack(pady=5)
               width_entry = tk.Entry(dimension_window, font=('Arial', 12))
               width_entry.pack(pady=5)
               calculate_button = tk.Button(dimension_window, text="Calculate", font=('Arial', 12),
                                            command=lambda: calculate_rectangle_area_perimeter(float(length_entry.get()), float(width_entry.get()), dimension_window))
               calculate_button.pack(pady=5)
           elif shape == "Circle":
               radius_label = tk.Label(dimension_window, text="Radius:", font=('Arial', 12))
               radius_label.pack(pady=5)
               radius_entry = tk.Entry(dimension_window, font=('Arial', 12))
               radius_entry.pack(pady=5)
               calculate_button = tk.Button(dimension_window, text="Calculate", font=('Arial', 12),command=lambda: calculate_circle_area_perimeter(float(radius_entry.get()), dimension_window))
               calculate_button.pack(pady=5)
           elif shape == "Triangle":
               side1_label = tk.Label(dimension_window, text="Side 1:", font=('Arial', 12))
               side1_label.pack(pady=5)
               side1_entry = tk.Entry(dimension_window, font=('Arial', 12))
               side1_entry.pack(pady=5)
               side2_label = tk.Label(dimension_window, text="Side 2:", font=('Arial', 12))
               side2_label.pack(pady=5)
               side2_entry = tk.Entry(dimension_window, font=('Arial', 12))
               side2_entry.pack(pady=5)
               side3_label = tk.Label(dimension_window, text="Side 3:", font=('Arial', 12))
               side3_label.pack(pady=5)
               side3_entry = tk.Entry(dimension_window, font=('Arial', 12))
               side3_entry.pack(pady=5)
               calculate_button = tk.Button(dimension_window, text="Calculate", font=('Arial', 12),
                                            command=lambda: calculate_triangle_area_perimeter(float(side1_entry.get()), float(side2_entry.get()), float(side3_entry.get()), dimension_window))
               calculate_button.pack(pady=5)

       def calculate_square_area_perimeter(side_length, window):
           area = side_length ** 2
           perimeter = 4 * side_length
           result_label.config(text=f"Area = {area}, Perimeter = {perimeter}")
           window.destroy()

       def calculate_rectangle_area_perimeter(length, width, window):
           area = length * width
           perimeter = 2 * (length + width)
           result_label.config(text=f"Area = {area}, Perimeter = {perimeter}")
           window.destroy()

       def calculate_circle_area_perimeter(radius, window):
           area = math.pi * radius ** 2
           perimeter = 2 * math.pi * radius
           result_label.config(text=f"Area = {area}, Perimeter = {perimeter}")
           window.destroy()

       def calculate_triangle_area_perimeter(side1, side2, side3, window):
           perimeter = side1 + side2 + side3
           area = 0.5 * side1 * side2
           result_label.config(text=f"Area = {area}, Perimeter = {perimeter}")
           window.destroy()

       

       root = tk.Tk()
       root.title("Calculator")
       root.configure(bg="#f0f0f0")

       entry = tk.Entry(root, width=30, borderwidth=5, font=('Arial', 14))
       entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipady=10)

       buttons = [
           ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
           ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
           ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
           ('0', 4, 0), ('.', 4, 1), ('+', 4, 3), ('√', 4, 2),
           ('^', 5, 0), ('shape', 5, 1), ('delete', 5, 2),
       ]
       for (text, row, column) in buttons:
           button = tk.Button(root, text=text, padx=20, pady=20, font=('Arial', 14), bg="BLUE" if text == "Notes" else "#d9d9d9", activebackground="#bfbfbf",command=lambda t=text: press_key(t) if t != "shape" and t != "Notes" else open_shape_window() if t == "shape" else open_notes_window() ) 
           if text == "delete":
               button.config(bg="#ff6347", activebackground="#ff6347", fg="white", padx=40, pady=10)
           button.grid(row=row, column=column, sticky="nsew")
           root.grid_columnconfigure(column, weight=1)


       clear_button = tk.Button(root, text="c", padx=20, pady=20, font=('Arial', 14), bg="#ff6347", activebackground="#ff6347",fg="white", command=clear)
       clear_button.grid(row=6, column=0, columnspan=2, sticky="nsew")
       root.grid_columnconfigure(0, weight=1)

       equal_button = tk.Button(root, text="=", padx=20, pady=20, font=('Arial', 14), bg="#3cb371", activebackground="#3cb371",
                                fg="white", command=calculate)
       equal_button.grid(row=6, column=2, columnspan=2, sticky="nsew")
       root.grid_columnconfigure(1, weight=1)

       result_label = tk.Label(root, text="", font=('Arial', 14), bg="#f0f0f0")
       result_label.grid(row=7, column=0, columnspan=4, pady=10)

       for i in range(8):
           root.grid_rowconfigure(i, weight=1)

       root.mainloop()

       response = "i do it for you"

       
    elif "note" in question.lower() :

      class NoteManager:
          def __init__(self):
              self.notes = []
              self.note_count = 0  
              self.load_notes()

          def add_note(self, title, content):
              now = datetime.datetime.now()

              new1 = now 

              timestamp = new1.strftime('%Y-%m-%d %H:%M:%S')
              
              self.notes.append({"title": title, "content": content, "timestamp": timestamp})
              self.note_count += 1  
              self.save_notes()  

          def load_notes(self):
              try:
                  with open("notes.json", "r") as file:
                      self.notes = json.load(file)
                      self.note_count = len(self.notes)
              except FileNotFoundError:
                  
                  self.notes = []
                  self.note_count = 0

          def save_notes(self):
              with open("notes.json", "w") as file:
                  json.dump(self.notes, file)

          def get_note_titles(self):
              return [note["title"] for note in self.notes]

          def get_note_content(self, title):
              for note in self.notes:
                  if note["title"] == title:
                      return note["content"]
              return None

          def get_note_timestamp(self, title):
              for note in self.notes:
                  if note["title"] == title:
                      return note["timestamp"]
              return None

          def update_note_content(self, title, new_title, new_content):
            for note in self.notes:
                if note["title"] == title:
                    note["title"] = new_title
                    note["content"] = new_content
                    timestamp1 = new1.strftime('%Y-%m-%d %H:%M:%S')
                    note["timestamp"] = timestamp1
                    self.save_notes()  
                    return True
            return False

          def delete_note_content(self, title):
            for note in self.notes:
                if note["title"] == title:
                    self.notes.remove(note)
                    self.note_count -= 1  
                    self.save_notes()  
                    return True
            return False
      class NoteApp:
          def __init__(self, root, note_manager):
                  self.root = root
                  self.note_manager = note_manager
                  self.root.title("Note App")
                  self.root.geometry("500x510")

                  self.style = ttk.Style()
                  self.style.configure("TButton", padding=10, font=("Arial", 12))
                  self.style.configure("TEntry", padding=6, font=("Arial", 12))
                  self.style.configure("TFrame", background="#f0f0f0")

                  self.search_window = None  

                  self.main_frame = ttk.Frame(root, padding=(20, 20))
                  self.main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

                  
                  self.add_button = tk.Button(self.main_frame, text="Add Note", width=15, bg="green", padx=10, pady=10, command=self.add_note)
                  self.add_button.grid(row=0, column=0, pady=10, padx=10, sticky="nsew")

                  self.edit_button = tk.Button(self.main_frame, text="Edit Note", width=15, bg="blue", padx=10, pady=10, command=self.show_edit_note_titles)
                  self.edit_button.grid(row=1, column=0, pady=10, padx=10, sticky="nsew")

                  self.note_count_label = tk.Label(self.main_frame, text=f"Total Notes: {len(self.note_manager.notes)}", font=("Arial", 12))
                  self.note_count_label.grid(row=2, column=0, pady=10, padx=10)

                  self.main_frame.grid_columnconfigure(0, weight=1)
                  self.main_frame.grid_rowconfigure(0, weight=1)
                  self.main_frame.grid_rowconfigure(1, weight=1)
                  self.main_frame.grid_rowconfigure(2, weight=1)
          def add_note(self):
              def save_note():
                  note_title = note_title_entry.get()
                  note_content = note_content_entry.get("1.0", tk.END)
                  if note_title.strip() != "" and note_content.strip() != "":
                      self.note_manager.add_note(note_title, note_content)
                      top.destroy()
                      self.update_note_count()
                      messagebox.showinfo("Success", "Note added successfully!")
                  else:
                      messagebox.showwarning("Warning", "Please enter both title and content for the note!")

              top = tk.Toplevel(self.root)
              top.title("Add Note")

              note_title_label = tk.Label(top, text="Note Title:")
              note_title_label.pack(pady=5)
              note_title_entry = ttk.Entry(top)
              note_title_entry.pack(pady=5)

              note_content_label = tk.Label(top, text="Note Content:")
              note_content_label.pack(pady=5)
              note_content_entry = tk.Text(top, wrap=tk.WORD, width=40, height=10, font=("Arial", 12))
              note_content_entry.pack(padx=10, pady=10)

              save_button = tk.Button(top, text="Save Note", width=15, bg="green", padx=10, pady=10, command=save_note)
              save_button.pack(pady=5)

          def show_edit_note_titles(self):
              note_titles = self.note_manager.get_note_titles()
              if note_titles:
                  self.search_window = tk.Toplevel(self.root)
                  self.search_window.title("Select Note to Edit")
                  self.search_window.geometry("400x510")

                  button_colors = ["blue", "green", "yellow", "coral", "salmon", "cyan"]

                  self.search_frame = ttk.Frame(self.search_window, padding=(20, 20))
                  self.search_frame.pack(side=tk.TOP, fill=tk.X)

                  self.search_entry = ttk.Entry(self.search_frame)
                  self.search_entry.pack(side=tk.LEFT, padx=10)

                  self.search_button = tk.Button(self.search_frame, text="Search", width=15, bg="lightblue", padx=10, pady=10, command=self.search_notes)
                  self.search_button.pack(side=tk.LEFT, padx=10)

                  self.scrollbar = ttk.Scrollbar(self.search_window, orient=tk.VERTICAL)
                  self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

                  self.note_frame = ttk.Frame(self.search_window)
                  self.note_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

                  self.note_canvas = tk.Canvas(self.note_frame, yscrollcommand=self.scrollbar.set)
                  self.note_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

                  self.scrollbar.config(command=self.note_canvas.yview)

                  self.inner_frame = ttk.Frame(self.note_canvas)
                  self.note_canvas.create_window((0, 0), window=self.inner_frame, anchor=tk.NW)

                  for index, title in enumerate(note_titles):
                      note_title_button = tk.Button(self.inner_frame, text=title, width=30, bg=button_colors[index % len(button_colors)], padx=10, pady=10, command=lambda t=title: self.edit_note_content(t))
                      note_title_button.pack(side=tk.TOP, padx=5, pady=2)

                  self.note_canvas.update_idletasks()
                  self.note_canvas.config(scrollregion=self.note_canvas.bbox("all"))
              else:
                  messagebox.showinfo("Info", "No notes available!")

          def edit_note_content(self, title):
              original_title = title
              original_content = self.note_manager.get_note_content(title)
              original_timestamp = self.note_manager.get_note_timestamp(title)

              if original_content:
                  top = tk.Toplevel(self.root)
                  top.title("Edit Note")
                  top.geometry("500x510")

                  def check_changes(event=None):
                      if note_title_entry.get() != original_title or note_content_entry.get("1.0", tk.END).strip() != original_content.strip():
                          save_button.pack(side=tk.LEFT, padx=5)
                      else:
                          save_button.pack_forget()

                  def save_changes():
                      new_title = note_title_entry.get()
                      new_content = note_content_entry.get("1.0", tk.END)
                      if new_title.strip() != "" and new_content.strip() != "":
                          self.note_manager.update_note_content(original_title, new_title, new_content)
                          top.destroy()
                          self.update_note_count()
                          messagebox.showinfo("Success", "Note updated successfully!")
                      else:
                          messagebox.showwarning("Warning", "Please enter both title and content for the note!")

                  def delete_note():
                      if self.note_manager.delete_note_content(original_title):
                          top.destroy()
                          self.update_note_count()
                          messagebox.showinfo("Success", "Note deleted successfully!")
                      else:
                          messagebox.showerror("Error", f"Note '{original_title}' not found!")

                  note_title_label = tk.Label(top, text="Note Title:")
                  note_title_label.pack(pady=5)
                  note_title_entry = ttk.Entry(top)
                  note_title_entry.insert(0,original_title)
                  note_title_entry.pack(pady=5)
                  note_title_entry.bind("<KeyRelease>", check_changes)

                  note_content_label = tk.Label(top, text="Note Content:")
                  note_content_label.pack(pady=5)
                  note_content_entry = tk.Text(top, wrap=tk.WORD, width=40, height=10, font=("Arial", 12))
                  note_content_entry.insert(tk.END, original_content)
                  note_content_entry.pack(padx=10, pady=10)
                  note_content_entry.bind("<KeyRelease>", check_changes)

                  timestamp_label = tk.Label(top, text=f"Saved on: {original_timestamp}", font=("Arial", 10, "italic"))
                  timestamp_label.pack(pady=5)

                  button_frame = ttk.Frame(top)
                  button_frame.pack(pady=5)

                  save_button = tk.Button(button_frame, text="Save Changes", width=15, bg="green", padx=10, pady=10, command=save_changes)
                  save_button.pack_forget()

                  delete_button = tk.Button(button_frame, text="Delete Note", width=15, bg="red", padx=10, pady=10, command=delete_note)
                  delete_button.pack(side=tk.LEFT, padx=5)

          def update_note_count(self):
              self.note_count_label.config(text=f"Total Notes: {len(self.note_manager.notes)}")

          def search_notes(self, event=None):
              search_term = self.search_entry.get().lower()
              note_titles = self.note_manager.get_note_titles()
              if search_term:
                  filtered_titles = [title for title in note_titles if search_term in title.lower()]
                  if filtered_titles:
                      self.show_notes(filtered_titles)
                  else:
                      messagebox.showinfo("Info", "No notes found with this title.")
              else:
                  self.show_notes(note_titles)

          def show_notes(self, note_titles):
              if self.search_window:
                  self.search_window.destroy()

              top = tk.Toplevel(self.root)
              top.title("Select Note to Edit")
              top.geometry("400x510")

              button_colors = ["blue", "green", "yellow", "coral", "salmon", "cyan"]

              note_canvas = tk.Canvas(top)
              note_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

              scrollbar = ttk.Scrollbar(top, orient=tk.VERTICAL, command=note_canvas.yview)
              scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

              inner_frame = ttk.Frame(note_canvas)
              note_canvas.create_window((0, 0), window=inner_frame, anchor=tk.NW)

              for index, title in enumerate(note_titles):
                  note_frame = ttk.Frame(inner_frame)
                  note_frame.pack(pady=5)

                  note_title_button = tk.Button(note_frame, text=title, width=30, bg=button_colors[index % len(button_colors)], padx=10, pady=10, command=lambda t=title: self.edit_note_content(t))
                  note_title_button.pack(side=tk.TOP, padx=5, pady=2)

              note_canvas.bind("<Configure>", lambda e: note_canvas.configure(scrollregion=note_canvas.bbox("all")))
              note_canvas.configure(yscrollcommand=scrollbar.set)
      response = "i do it for you"

      root = tk.Tk()
      note_manager = NoteManager()
      app = NoteApp(root, note_manager)
      root.mainloop()

      response = "i do it for you"
    elif "translat" in question.lower() :
        response = ""
        def translate_word():
            word = entry6.get().lower()

            if word == "code":
                translated_word.set("كود")
            elif word == "play":
                translated_word.set("يلعب")
            elif word == "do" or word == "does":
                translated_word.set("يفعل")
            elif word == "have" or word == "has":
              translated_word.set("يملك")
            elif word == "mustafa hazem":
              translated_word.set("مصطفى حازم")
            elif word == "boy":
              translated_word.set("ولد")
            elif word == "girl":
              translated_word.set("بنت")
            elif word == "white":
              translated_word.set("أبيض")
            elif word == "black":
              translated_word.set("أسود")
            elif word == "red":
              translated_word.set("أحمر")
            elif word == "doctor":
              translated_word.set("طبيب")
            elif word == "nurse":
              translated_word.set("ممرضة")
            elif word == "green":
              translated_word.set("أخضر")
            elif word == "good":
              translated_word.set("جيد")
            elif word == "cat":
              translated_word.set("قطة")
            elif word == "dog":
              translated_word.set("كلب")
            elif word == "fish":
              translated_word.set("سمكة")
            elif word == "bird":
              translated_word.set("طائر")
            elif word == "car":
              translated_word.set("سيارة")
            elif word == "apple":
              translated_word.set("تفاحة")
            elif word == "banana":
              translated_word.set("موزة")
            elif word == "computer":
              translated_word.set("كمبيوتر")
            elif word == "keyboard":
              translated_word.set("لوحة مفاتيح")
            elif word == "book":
              translated_word.set("كتاب")
            elif word == "table":
              translated_word.set("طاولة")
            elif word == "chair":
              translated_word.set("كرسي")
            elif word == "school":
              translated_word.set("مدرسة")
            elif word == "student":
              translated_word.set("طالب")
            elif word == "teacher":
              translated_word.set("معلم")
            elif word == "pencil":
              translated_word.set("قلم رصاص")
            elif word == "pen":
              translated_word.set("قلم حبر")
            elif word == "bag":
              translated_word.set("حقيبة")
            elif word == "phone":
              translated_word.set("هاتف")
            elif word == "home":
              translated_word.set("منزل")
            elif word == "bed":
              translated_word.set("سرير")
            elif word == "ball":
              translated_word.set("كرة")
            elif word == "sun":
              translated_word.set("شمس")
            elif word == "moon":
              translated_word.set("قمر")
            elif word == "star":
              translated_word.set("نجمة")
            elif word == "water":
              translated_word.set("ماء")
            elif word == "tree":
              translated_word.set("شجرة")
            elif word == "flower":
              translated_word.set("زهرة")
            elif word == "sky":
              translated_word.set("سماء")
            elif word == "earth":
              translated_word.set("أرض")
            elif word == "fire":
              translated_word.set("نار")
            elif word == "air":
              translated_word.set("هواء")
            elif word == "hello":
              translated_word.set("مرحبا")
            elif word == "welcome":
              translated_word.set("مرحبا")
            elif word == "hi" or word == "hey" or word == "hy" :
              translated_word.set("مرحبا")
            elif word == "mountain":
              translated_word.set("جبل")
            elif word == "road":
              translated_word.set("طريق")
            elif word == "house":
              translated_word.set("بيت")
            elif word == "door":
              translated_word.set("باب")
            elif word == "window":
              translated_word.set("نافذة")
            elif word == "mirror":
              translated_word.set("مرآة")
            elif word == "table":
              translated_word.set("طاولة")
            elif word == "chair":
              translated_word.set("كرسي")
            elif word == "bedroom":
              translated_word.set("غرفة نوم")
            elif word == "kitchen":
              translated_word.set("مطبخ")
            elif word == "bathroom":
              translated_word.set("حمام")
            elif word == "living room":
              translated_word.set("غرفة معيشة")
            elif word == "dining room":
              translated_word.set("غرفة طعام")
            elif word == "closet":
              translated_word.set("خزانة")
            elif word == "stove":
              translated_word.set("موقد")
            elif word == "refrigerator":
              translated_word.set("ثلاجة")
            elif word == "microwave":
              translated_word.set("ميكروويف")
            elif word == "oven":
              translated_word.set("فرن")
            elif word == "i":
              translated_word.set("أنا")
            elif word == "you":
              translated_word.set("أنت")
            elif word == "he":
              translated_word.set("هو")
            elif word == "she":
              translated_word.set("هي")
            elif word == "it":
              translated_word.set("هو لغير عاقل")
            elif word == "we":
              translated_word.set("نحن")
            elif word == "they":
              translated_word.set("هم")
            elif word == "love":
              translated_word.set("حب")
            elif word == "hate":
              translated_word.set("يكرره")
            elif word == "friend":
              translated_word.set("صديق")
            elif word == "family":
              translated_word.set("عائلة")
            elif word == "school":
              translated_word.set("مدرسة")
            elif word == "class":
              translated_word.set("فصل")
            elif word == "teacher":
              translated_word.set("معلم")
            elif word == "student":
              translated_word.set("طالب")
            else:
              translated_word.set("Sorry, I don't know this word.\n It will be added soon to my dictionary\n if it has a meaning.")

        root1 = tk.Toplevel()  
        root1.title("English to Arabic Translator")
        root1.geometry("400x300")
        root1.resizable(False, False)

        label1 = tk.Label(root1, text="I can translate word from ENGLISH to ARABIC", font=("Arial", 12))
        label1.pack(pady=(20, 1))

        label = tk.Label(root1, text="Enter the word:", font=("Arial", 13))
        label.pack(pady=(20, 3))

        entry6 = tk.Entry(root1, font=("Arial", 14))
        entry6.pack(ipady=3)

        translate_button = tk.Button(root1, text="Translate",width=button_width,bg="green", padx=button_padding, pady=button_padding, command=translate_word, font=("Arial", 13))
        translate_button.pack(pady=10)

        translated_word = tk.StringVar()
        translation_label = tk.Label(root1, textvariable=translated_word, font=("Arial", 15))
        translation_label.pack(pady=(10, 20))

        root1.mainloop()
        response = "i do it for you"
    elif "repeat" in question.lower():
        response = ""
        def print_word():
            word = entry_word.get()
            try:
              num = int(entry_num.get())
              if num <= 0:
                raise ValueError("Please enter a positive integer")
              for _ in range(num):
                textbox.insert(tk.END, word + "\n")
              textbox.insert(tk.END, "The end\n\n")
            except ValueError as e:
                messagebox.showinfo("Info", "Pleas try again")
              
        window = tk.Tk()
        window.title("REPEAT")
        window.geometry("400x600")

        label_word = tk.Label(window, text="Enter a word:")
        label_word.pack()
        entry_word = tk.Entry(window)
        entry_word.pack()

        label_num = tk.Label(window, text="Enter a number:")
        label_num.pack()
      
        entry_num = tk.Entry(window)
        entry_num.pack()

        print_button = tk.Button(window, text="Print",width=button_width, bg="green",padx=button_padding, pady=button_padding, command=print_word)
        print_button.pack(pady=10)

        textbox = tk.Text(window)
        textbox.pack()

        window.mainloop()
        response = "i do it for you"
    elif "time" in question.lower() or "minute" in question.lower() or "date" in question.lower():
       root = tk.Tk()
       root.title("time")
       root.configure(bg="lightgray")

       canvas = Canvas(root, width=300, height=300, bg='lightgray', highlightthickness=0)
       canvas.grid(row=0, column=0, padx=10, pady=10)

       def draw_clock():   
           canvas.delete("all")
           center_x, center_y = 150, 150
           radius = 120

           canvas.create_oval(center_x - radius, center_y - radius, center_x + radius, center_y + radius, outline="black", width=4, fill='lightblue')

           for i in range(1, 13):
               angle = math.radians(i * 30 - 90)
               x = center_x + (radius - 25) * math.cos(angle)
               y = center_y + (radius - 25) * math.sin(angle)
               canvas.create_text(x, y, text=str(i), font=('calibri', 20, 'bold'), fill='purple')

           time_now = localtime()
           hour = (time_now.tm_hour ) % 12
           minute = time_now.tm_min
           second = time_now.tm_sec

           hour_angle = math.radians((hour * 30) - 90 + (minute / 2))
           hour_length = radius * 0.5
           hour_x = center_x + hour_length * math.cos(hour_angle)
           hour_y = center_y + hour_length * math.sin(hour_angle)

           canvas.create_line(center_x, center_y, hour_x, hour_y, fill="darkblue", width=6, capstyle=tk.ROUND)

           minute_angle = math.radians((minute * 6) - 90)
           minute_length = radius * 0.7
           minute_x = center_x + minute_length * math.cos(minute_angle)
           minute_y = center_y + minute_length * math.sin(minute_angle)

           canvas.create_line(center_x, center_y, minute_x, minute_y, fill="darkblue", width=4, capstyle=tk.ROUND)

           second_angle = math.radians((second * 6) - 90)
           second_length = radius * 0.9
           second_x = center_x + second_length * math.cos(second_angle)
           second_y = center_y + second_length * math.sin(second_angle)

           canvas.create_line(center_x, center_y, second_x, second_y, fill="red", width=2, capstyle=tk.ROUND)

           root.after(1000, draw_clock)

       draw_clock()

       label_time = tk.Label(root, font=('calibri', 20, 'bold'), background='purple', foreground='white')
       label_time.grid(row=1, column=0, padx=10, pady=10)

       def display_time():
           now1 = datetime.datetime.now()
           new11 = now1
           now31 = new11.strftime('%I:%M:%S %p')
           label_time.config(text=now31)
           label_time.after(1000, display_time)

       display_time()

       label_date = tk.Label(root, font=('calibri', 20, 'bold'), background='purple', foreground='white')
       label_date.grid(row=2, column=0, padx=10, pady=10)

       def display_date():
           current_date = strftime('%A, %d %B %Y', localtime())
           label_date.config(text=current_date)

       display_date()

       root.mainloop()
       response = "i do it for you"
    elif "sound" in question.lower():
       def cs():
           question11 = q11.get()

           if not question11.strip():
               messagebox.showinfo("Info", "Please enter your text!")
               q11.delete(0, tk.END)
           else:
               text = question11
               if text:
            
                   engine = pyttsx3.init()
            
            
                   engine.setProperty('rate', 150)  
                   engine.setProperty('volume', 1)  

            
                   engine.say(text)
                   engine.runAndWait()

               q11.delete(0, tk.END)


       mhd13 = tk.Tk()
       mhd13.title("Text-to-Speech App")
       mhd13.geometry("530x300")


       frames = [ttk.Frame(mhd13) for _ in range(6)]
       for frame in frames:
         frame.pack(pady=10, fill="both")


       random_label911 = tk.Label(frames[2], text="MHD", font=("Arial", 17))
       random_label911.pack()

       qe = tk.Label(frames[3], text="Enter the text you want to convert to speech:", font=("Arial", 15))
       qe.pack()

       q11 = tk.Entry(frames[3], width=50)
       q11.pack()

       sent = tk.Button(frames[3], text="ENTER", bg="green", fg="white", padx=10, pady=10, command=cs)
       sent.pack()

       mhd13.mainloop()



       response = "i do it for you"
    elif "mhd" in question.lower():
      response = "What do you need for me to do ?"

    else:
        response = "I don't understand your question"
    return response

def ask_user_name():
    global user_name
    user_name = q6.get()
    if user_name.strip() == "":
        user_name = "YOU"
        mhd16.destroy()
    else:
        pygame.mixer.init()
        user_name = q6.get()
        ree = "welcome" + user_name 
        tts = gTTS(ree, lang='en')
        last_sound_file_path1 = "last_r1.mp3"
        
        tts.save(last_sound_file_path1)

        pygame.mixer.music.load(last_sound_file_path1)
        pygame.mixer.music.play()
    mhd16.destroy()
def ask_question():
    global last_sound_file_path

    question = q.get()
    response = mhd(question)

    if question.strip() == "":
        messagebox.showinfo("Info", "Please enter your question!")
    else:
        r.insert(tk.END, str(user_name).upper() + " :", 'mhd_font')
        r.insert(tk.END, str(space) + str(now3) + "\n")
        r.insert(tk.END, str(question) + "\n\n")
        r.insert(tk.END, str(mhd9) + "\n", 'mhd_font')
        r.insert(tk.END, str(response) + "\n\n\n")

        
        tts = gTTS(response, lang='en')
        last_sound_file_path = "last_response55.mp3"

        
        if os.path.exists(last_sound_file_path):
            pygame.mixer.music.unload()
            os.remove(last_sound_file_path)
        
        tts.save(last_sound_file_path)

        
        pygame.mixer.music.load(last_sound_file_path)
        pygame.mixer.music.play()

    q.delete(0, tk.END)

def toggle_recording():
    if recording_thread.is_recording:
        recording_thread.stop_recording()
        update_status("Recording stopped", "red")
    else:
        recording_thread.start_recording()
        update_status("Recording started", "green")

class RecordingThread(threading.Thread):
    def __init__(self):
        super().__init__()
        self.is_recording = False
        self.recognizer = sr.Recognizer()
        self.daemon = True

    def run(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            while self.is_recording:
                try:
                    audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=5)
                    question = self.recognizer.recognize_google(audio)
                    q.delete(0, tk.END)
                    q.insert(0, question)
                    ask_question()
                except sr.UnknownValueError:
                    update_status("Could not understand audio", "red")
                except sr.RequestError as e:
                    update_status(f"Error: {e}", "red")
                except sr.WaitTimeoutError:
                    update_status("Listening timed out", "red")

    def start_recording(self):
        if not self.is_recording:
            self.is_recording = True
            self.start()

    def stop_recording(self):
        self.is_recording = False

def update_status(message, color):
    status_label.config(text=message, foreground=color)





mhd16 = tk.Tk()
mhd16.title("ENTER YOUR NAME")
mhd16.geometry("530x700")

qe6 = Label(mhd16, text="ENTER YOUR NAME!", font=("Arial", 10))
qe6.pack()

q6 = Entry(mhd16, width=50)
q6.pack()

sent6 = Button(mhd16, text="ENTER", bg="green", fg="white", padx=10, pady=10, command=ask_user_name)
sent6.pack()

mhd16.mainloop()

mhd1 = tk.Tk()
mhd1.title("MHD-CHATBOT")
mhd1.geometry("530x700")


responses11 = [
    "Hello!",
    "Hey!",
    "Welcome!",
    "Hi!",
    "How can I help you?",
    "What can I do for you?",
]
response1 = random.choice(responses11)
random_label = Label(mhd1, text=response1, font=("Arial", 20))
random_label.pack()

qe = Label(mhd1, text="Ask me anything!", font=("Arial", 10))
qe.pack()

q = Entry(mhd1, width=50)
q.pack()

sent = Button(mhd1, text="ASK",  width=button_width, bg="green",padx=6, pady=8,  command=ask_question)
sent.pack()

record_button = Button(mhd1, text="Record", width=button_width, bg="blue", padx=6, pady=8, command=toggle_recording)
record_button.pack()

status_label = Label(mhd1, text="Press the button to start recording.", foreground="gray")
status_label.pack()


r = tk.Text(mhd1, width=60, height=20, font=("Arial", 12))
r.tag_configure('mhd_font', font=("Arial", 13, 'bold'))  
r.pack()

def open_window(title, message):
  window = tk.Toplevel(mhd1)
  window.title(title)
  window.geometry("400x500")

  label = tk.Label(window, text=message, wraplength=380, justify="left")
  label.pack(pady=20)

def open_window5():
  message = "I answer most of your questions. Please enter your question."
  open_window("Answer Question", message)

def open_window6():
  message = """To display a calculator, write “I need a calculator” in the question.
  Choose numbers for addition (+), for multiplication (*), for subtraction (-), for division (/), exponents (^), and root.
  Press (✓) and write the number and its root type to calculate perimeter and area.
  For some shapes, click on (shape) and choose the shape.
  If it is a square, write the length of its side.
  If it is a circle, write half the length of its diameter.
  If it is a rectangle, write its length and width.
  If it is a triangle, write the length of its first, second, and last side."""
  open_window("Calculated", message)

def open_window7():
  message = """To display a translator, write “I need a translator” in the question.
  Write the word you want to translate in English then click on (translate)."""
  open_window("Translate", message)

def open_window8():
  message = """To display a repeat, write “I need a repeat” in the question.
  Write the word you want to repeat and write the number of repeats then click on (print)."""
  open_window("Repeat", message)

def open_window9():
  message = """To display notes, write “I need a note” in the question.
  To add notes click on (add note) and write the note then click on (save note) to save the note.
  To read the note click on (view note), to change the note click on (change note), select the note you want to change,
  write the new note, and click on (save change) to save the change.
  To delete the note click on (delete note), select the note you want to delete and click on (delete)."""
  open_window("Notes", message)

def open_window10():
  import os

  file_path = "index.html"
  chrome_path = ""
  os.system(chrome_path % file_path)


def open_window11():
  message = "I am MHD, a chat bot created by Mostafa Hazem. I was created in 2024."
  open_window("About", message)

def open_window12():
  message = """To display time, write “I need a time” in the question.
  This time is Egypt time and summer time.
  """
  open_window("About", message)

def open_window4():
    window1 = tk.Toplevel(mhd1)
    window1.title("helping")
    window1.geometry("400x400")

    qe5 = Label(window1, text="Where are you facing the problem?", font=("Arial", 10))
    qe5.pack()

    button5 = tk.Button(window1, text="Answer the question", width=button_width,bg="red", padx=button_padding, pady=button_padding, command=open_window5)
    button5.pack(pady=(button_distance, 0))

    button6 = tk.Button(window1, text="calculated", width=button_width, bg="blue",padx=button_padding, pady=button_padding, command=open_window6)
    button6.pack(pady=(button_distance, 0))

    button7 = tk.Button(window1, text="translated", width=button_width, bg="yellow",padx=button_padding, pady=button_padding, command=open_window7)
    button7.pack(pady=(button_distance, 0))

    button8 = tk.Button(window1, text="repeat", width=button_width, bg="purple",padx=button_padding, pady=button_padding, command=open_window8)
    button8.pack(pady=(button_distance, 0))

    button12 = tk.Button(window1, text="time", width=button_width, bg="coral",padx=button_padding, pady=button_padding, command=open_window12)
    button12.pack(pady=(button_distance, 0))

    button9 = tk.Button(window1, text="note", width=button_width, bg="orange",padx=button_padding, pady=button_padding, command=open_window9)
    button9.pack(pady=(button_distance, 0))

    button10 = tk.Button(window1, text="chat us", width=button_width, bg="green",padx=button_padding, pady=button_padding, command=open_window10)
    button10.pack(pady=(button_distance, 0))

    button11 = tk.Button(window1, text="about", width=button_width, bg="maroon",padx=button_padding, pady=button_padding, command=open_window11)
    button11.pack(pady=(button_distance, 0))

button4 = tk.Button(mhd1, text="helping",  width=button_width, bg="red",padx=button_padding, pady=button_padding,  command=open_window4)
button4.pack()



recording_thread = RecordingThread()
mhd1.mainloop()
                                                    
                                                             #THE_END#                            
