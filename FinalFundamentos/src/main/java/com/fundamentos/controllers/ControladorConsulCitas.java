package com.fundamentos.controllers;

import com.fundamentos.models.DatosConsulCita;
import java.util.ArrayList;

public class ControladorConsulCitas {
    ArrayList<DatosConsulCita> arregloCitas2;
    
    public ControladorConsulCitas(ArrayList<DatosConsulCita> arregloCitas2){
        this.arregloCitas2 = arregloCitas2;
    }
    
    public DatosConsulCita obtenerCita(int numCita){
        return arregloCitas2.get(numCita);
    }
    
    public int getTamañoArreglo(){
        return arregloCitas2.size();
    }
}

