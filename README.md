<div align="center">
  <h1>📱 Generador de Códigos QR</h1>
  <p><em>Solución para la creación y gestión de códigos QR Estáticos y Dinámicos (Tradicional e Híbrido).</em></p>
  <img src="https://img.shields.io/badge/VERSI%C3%93N-BETA_02%2F04%2F2026-orange?style=flat-square" alt="Versión">
</div>

<hr>

<h2>📖 Descripción de Versiones</h2>
<p>Este repositorio incluye diferentes implementaciones probadas en entornos locales, adaptables según los requerimientos de persistencia y conectividad del proyecto.</p>

<h3>🔄 Códigos QR Dinámicos</h3>
<p>Incluye dos variantes principales orientadas a la actualización en tiempo real:</p>
<ul>
  <li><strong>v1A (Versión Tradicional):</strong> Diseñada para simular un entorno de servidor real. La lógica está conectada a una base de datos local montada sobre <strong>XAMPP</strong>.
    <blockquote style="border-left: 4px solid #8250df; padding-left: 10px; color: #57606a;">
      <p><strong style="color: #8250df;">🪧 Important</strong><br>
      <strong>Requisito de Conexión:</strong> En esta versión, el código QR está enlazado directamente al servidor local. Si el servidor se apaga o pierde conectividad, el código QR dejará de funcionar y no redirigirá a ningún sitio.</p>
    </blockquote>
  </li>
  <li><strong>v1B (Versión Híbrida):</strong> Funciona mediante la integración de una API Key de <strong>TinyURL</strong> combinada con la base de datos local. El sistema se comunica con la API para actualizar el estado del QR.
    <blockquote style="border-left: 4px solid #0969da; padding-left: 10px; color: #57606a;">
      <p><strong style="color: #0969da;">ℹ️ Note</strong><br>
      <strong>Autonomía:</strong> Esta versión permite que el código exista y funcione sin depender de una conexión constante con el servidor local. Si la ruta no necesita ser modificada a futuro, actuará en la práctica como un QR estático.</p>
    </blockquote>
  </li>
</ul>

<h3>📌 Códigos QR Estáticos</h3>
<ul>
  <li><strong>Versión Base:</strong> Mantiene la funcionalidad de la v01 sin alteraciones. Es la opción más segura, rápida y práctica para generar códigos QR permanentes en situaciones donde la información de destino no requiera ser editada.</li>
</ul>

<blockquote style="border-left: 4px solid #cf222e; padding-left: 10px; color: #57606a;">
  <p><strong style="color: #cf222e;">⚠️ Caution</strong><br>
  <strong>Advertencia de Desarrollo:</strong> Estas versiones corresponden a un entorno de prueba y los códigos pueden contener errores o <em>bugs</em> no documentados (Fecha de revisión: 02/04/2026).</p>
</blockquote>

<p align="right"><em>By: Vicente Aguilar</em></p>
