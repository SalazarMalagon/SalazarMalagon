package com.api.backend.repository;


import java.util.List;


import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;
import org.springframework.stereotype.Repository;

import com.api.backend.model.Reserva;

@Repository
public interface ReservaRepository extends JpaRepository<Reserva, String>{
    
    public List<Reserva> findBykIdusuario(Long kIdusuario);

    @Query("SELECT r.nCalificacion FROM Reserva r WHERE r.kIdrecurso = :kIdrecurso AND r.nEstadoreserva = :nEstadoreserva")
    public List<Integer> findCalificacion(@Param("kIdrecurso") int kIdrecurso, @Param("nEstadoreserva") String nEstadoreserva);
}
