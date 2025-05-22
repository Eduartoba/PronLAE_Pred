from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.scrollview import ScrollView
import pandas as pd
import numpy as np
import random
import os

def evolucionar_fases(df_historial, generaciones=5, tamano_poblacion=100):
    pool_base = pd.Series(df_historial.values.ravel()).dropna().astype(int)
    frecuencia = pool_base.value_counts()
    base_nums = frecuencia.index.tolist()
    poblacion = [tuple(sorted(random.sample(base_nums, 5))) for _ in range(tamano_poblacion)]
    generaciones_fases = []
    for _ in range(generaciones):
        nueva_generacion = []
        for _ in range(tamano_poblacion):
            padre = list(random.choice(poblacion))
            idx_mutar = random.randint(0, 4)
            mutantes_posibles = list(set(range(1, 51)) - set(padre))
            random.shuffle(mutantes_posibles)
            padre[idx_mutar] = mutantes_posibles[0]
            nueva_generacion.append(tuple(sorted(padre)))
        generaciones_fases.append(nueva_generacion)
        poblacion = nueva_generacion
    return generaciones_fases[-1]

class EvolucionApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)
        self.label = Label(text="Selecciona archivo CSV con fases históricas:", size_hint=(1, 0.1))
        layout.add_widget(self.label)
        self.filechooser = FileChooserIconView(size_hint=(1, 0.4))
        layout.add_widget(self.filechooser)
        self.result_label = Label(text="", size_hint=(1, 0.1))
        layout.add_widget(self.result_label)
        self.run_button = Button(text="Ejecutar Predicción Evolutiva", size_hint=(1, 0.1))
        self.run_button.bind(on_press=self.run_prediction)
        layout.add_widget(self.run_button)
        self.output_area = Label(text="", size_hint=(1, 0.3))
        self.scroll = ScrollView(size_hint=(1, 0.4))
        self.scroll.add_widget(self.output_area)
        layout.add_widget(self.scroll)
        return layout

    def run_prediction(self, instance):
        if not self.filechooser.selection:
            self.result_label.text = "Selecciona un archivo primero."
            return
        try:
            df = pd.read_csv(self.filechooser.selection[0], header=None)
            resultado = evolucionar_fases(df)
            texto = "\n".join([str(r) for r in resultado])
            self.output_area.text = "Predicción:\n" + texto
            ruta = "/sdcard/Prediccion_Evolutiva_Final.csv"
            pd.DataFrame(resultado).to_csv(ruta, index=False, header=False)
            self.result_label.text = f"Guardado en: {ruta}"
        except Exception as e:
            self.result_label.text = f"Error: {str(e)}"

if __name__ == '__main__':
    EvolucionApp().run()
