import React from 'react';
import '../styles/Navbar.css';
import searchIcon from '../pictures/download.svg';
import lenguageIcon from '../pictures/traduccion.svg';

function Navbar() {
  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <span><a href="http://localhost:3000/">IsisGruop</a></span>
      </div>
      <div className="navbar-search">
        <input type="text" placeholder="Búsqueda" />
        <img src={searchIcon} alt="Buscar" className="search-icon" />
      </div>
      <div className="navbar-links">
        <a href="#learn"><img src={lenguageIcon} alt="lenguaje" className="lenguage-icon" /></a>
        <a href="#reference">Informacion</a>
        <a href="#community">Comunidad</a>
        <a href="#blog">Contactanos</a>
      </div>
    </nav>
  );
}

export default Navbar;
