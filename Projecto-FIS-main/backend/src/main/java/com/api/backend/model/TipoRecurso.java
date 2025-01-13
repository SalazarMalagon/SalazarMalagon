package com.api.backend.model;

import jakarta.persistence.Entity;
import jakarta.persistence.GeneratedValue;
import jakarta.persistence.GenerationType;
import jakarta.persistence.Id;
import jakarta.persistence.Table;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

@Entity
@Data
@AllArgsConstructor
@NoArgsConstructor
@Table(name = "tipoDeRecurso")
public class TipoRecurso {
    
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    int kIdtiporecurso;
    String nNombretiporecurso;
    String nDescripciontiporecurso;
    String nImagen;
}
