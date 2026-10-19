document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('form-archivo');
    const input = document.getElementById('archivo');
    const dropZone = document.getElementById('drop-zone');
    const nombreArchivo = document.getElementById('nombre-archivo');
    const btnProcesar = document.getElementById('btn-procesar');
    const zonaSubida = document.getElementById('zona-subida');
    const zonaCarga = document.getElementById('zona-carga');
    const zonaResultado = document.getElementById('zona-resultado');
    const zonaError = document.getElementById('zona-error');
    const btnDescargar = document.getElementById('btn-descargar');
    const resumenDatos = document.getElementById('resumen-datos');
    const mensajeError = document.getElementById('mensaje-error');

    // Click en la zona → abre el selector de archivos
    dropZone.addEventListener('click', () => input.click());

    // Arrastrar y soltar
    ['dragenter', 'dragover'].forEach(ev => {
        dropZone.addEventListener(ev, e => {
            e.preventDefault();
            dropZone.classList.add('dragover');
        });
    });
    ['dragleave', 'drop'].forEach(ev => {
        dropZone.addEventListener(ev, e => {
            e.preventDefault();
            dropZone.classList.remove('dragover');
        });
    });
    dropZone.addEventListener('drop', e => {
        const archivos = e.dataTransfer.files;
        if (archivos.length > 0) {
            input.files = archivos;
            manejarSeleccion();
        }
    });

    input.addEventListener('change', manejarSeleccion);

    function manejarSeleccion() {
        if (input.files.length > 0) {
            nombreArchivo.textContent = '📎 ' + input.files[0].name;
            btnProcesar.disabled = false;
        }
    }

    // Envío al backend
    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        if (!input.files[0]) return;

        zonaSubida.classList.add('hidden');
        zonaError.classList.add('hidden');
        zonaResultado.classList.add('hidden');
        zonaCarga.classList.remove('hidden');

        const formData = new FormData();
        formData.append('archivo', input.files[0]);

        try {
            const res = await fetch('/procesar', { method: 'POST', body: formData });
            const data = await res.json();

            zonaCarga.classList.add('hidden');

            if (!res.ok || data.error) {
                mostrarError(data.error || 'Error desconocido');
                return;
            }
            mostrarResultado(data);

        } catch (err) {
            zonaCarga.classList.add('hidden');
            mostrarError('No se pudo conectar con el servidor: ' + err.message);
        }
    });

    function mostrarResultado(data) {
        resumenDatos.innerHTML = '';

        agregarFilaResumen('Filas procesadas', data.resumen.filas);
        agregarFilaResumen('Columnas', data.resumen.columnas);

        data.resumen.numericas.forEach(num => {
            agregarFilaResumen(`${num.columna} (suma)`, num.suma.toFixed(2));
        });

        btnDescargar.href = '/descargar/' + data.reporte;
        zonaResultado.classList.remove('hidden');
        zonaResultado.scrollIntoView({ behavior: 'smooth' });
    }

    function agregarFilaResumen(etiqueta, valor) {
        const div = document.createElement('div');
        div.className = 'resumen-item';
        div.innerHTML = `<span>${etiqueta}</span><strong>${valor}</strong>`;
        resumenDatos.appendChild(div);
    }

    function mostrarError(msg) {
        mensajeError.textContent = msg;
        zonaError.classList.remove('hidden');
        zonaSubida.classList.remove('hidden');
        zonaSubida.scrollIntoView({ behavior: 'smooth' });
    }
});

