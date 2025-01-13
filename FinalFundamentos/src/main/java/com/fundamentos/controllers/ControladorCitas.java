package com.fundamentos.controllers;

import java.util.ArrayList;
import com.fundamentos.models.DatosSolicCita;

public class ControladorCitas {
    
    ArrayList<DatosSolicCita> arregloCitas;
    
    public ControladorCitas(ArrayList<DatosSolicCita> arregloCitas){
        this.arregloCitas = arregloCitas;
    }
    
    public DatosSolicCita obtenerCita(int numCita){
        return arregloCitas.get(numCita);
    }
    
    public int getTamañoArreglo(){
        return arregloCitas.size();
    }
}
