// static/js/script.js
document.addEventListener('DOMContentLoaded', function() {
    const fileInput = document.getElementById('file');
    const previewContainer = document.getElementById('preview-container');
    const previewImage = document.getElementById('image-preview');
    const uploadForm = document.getElementById('upload-form');

    fileInput.addEventListener('change', function() {
        const file = this.files[0];

        if (file) {
            const reader = new FileReader();

            reader.addEventListener('load', function() {
                previewImage.setAttribute('src', this.result);
                previewContainer.style.display = 'block';
            });

            reader.readAsDataURL(file);
        }
    });

    uploadForm.addEventListener('submit', function(e) {
        const fileInput = document.getElementById('file');
        if (!fileInput.files.length) {
            e.preventDefault();
            alert('Please select an image file');
        }
    });
});