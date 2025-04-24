import os
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from PIL import Image
import io
from django.core.files.uploadedfile import InMemoryUploadedFile

# Constantes pour les validations
IMAGE_MAX_SIZE_MB = 5  # Taille maximale des images en MB
AUDIO_MAX_SIZE_MB = 20  # Taille maximale des fichiers audio en MB
ALLOWED_IMAGE_EXTENSIONS = ['.jpg', '.jpeg', '.png', '.gif']
ALLOWED_AUDIO_EXTENSIONS = ['.mp3', '.wav', '.ogg', '.m4a']
ALLOWED_IMAGE_CONTENT_TYPES = ['image/jpeg', 'image/png', 'image/gif']
ALLOWED_AUDIO_CONTENT_TYPES = ['audio/mpeg', 'audio/wav', 'audio/ogg', 'audio/mp4']

# Dimensions maximales pour les images
MAX_WIDTH = 1200
MAX_HEIGHT = 1200
THUMBNAIL_SIZE = (300, 300)  # Pour les miniatures

def validate_image_file(file):
    """
    Valide le type et la taille d'un fichier image.
    
    Args:
        file: Le fichier à valider
        
    Raises:
        ValidationError: Si le fichier n'est pas valide
    """
    # Vérifier l'extension du fichier
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in ALLOWED_IMAGE_EXTENSIONS:
        raise ValidationError(
            _('Format de fichier non supporté. Les formats autorisés sont: %(extensions)s'),
            params={'extensions': ', '.join(ALLOWED_IMAGE_EXTENSIONS)},
        )
    
    # Vérifier le type MIME
    if hasattr(file, 'content_type') and file.content_type not in ALLOWED_IMAGE_CONTENT_TYPES:
        raise ValidationError(
            _('Type de contenu non supporté. Les types autorisés sont: %(types)s'),
            params={'types': ', '.join(ALLOWED_IMAGE_CONTENT_TYPES)},
        )
    
    # Vérifier la taille du fichier
    if file.size > IMAGE_MAX_SIZE_MB * 1024 * 1024:
        raise ValidationError(
            _('La taille du fichier ne doit pas dépasser %(size)s MB'),
            params={'size': IMAGE_MAX_SIZE_MB},
        )

def validate_audio_file(file):
    """
    Valide le type et la taille d'un fichier audio.
    
    Args:
        file: Le fichier à valider
        
    Raises:
        ValidationError: Si le fichier n'est pas valide
    """
    # Vérifier l'extension du fichier
    ext = os.path.splitext(file.name)[1].lower()
    if ext not in ALLOWED_AUDIO_EXTENSIONS:
        raise ValidationError(
            _('Format de fichier non supporté. Les formats autorisés sont: %(extensions)s'),
            params={'extensions': ', '.join(ALLOWED_AUDIO_EXTENSIONS)},
        )
    
    # Vérifier le type MIME
    if hasattr(file, 'content_type') and file.content_type not in ALLOWED_AUDIO_CONTENT_TYPES:
        raise ValidationError(
            _('Type de contenu non supporté. Les types autorisés sont: %(types)s'),
            params={'types': ', '.join(ALLOWED_AUDIO_CONTENT_TYPES)},
        )
    
    # Vérifier la taille du fichier
    if file.size > AUDIO_MAX_SIZE_MB * 1024 * 1024:
        raise ValidationError(
            _('La taille du fichier ne doit pas dépasser %(size)s MB'),
            params={'size': AUDIO_MAX_SIZE_MB},
        )

def optimize_image(image_field):
    """
    Optimise une image en la redimensionnant et en la compressant.
    
    Args:
        image_field: Le champ d'image à optimiser
        
    Returns:
        InMemoryUploadedFile: L'image optimisée
    """
    # Ouvrir l'image avec Pillow
    img = Image.open(image_field)
    
    # Conserver le format d'origine
    if img.format not in ['JPEG', 'PNG']:
        img_format = 'JPEG'  # Format par défaut
    else:
        img_format = img.format
    
    # Convertir en RGB si nécessaire (pour les images avec transparence)
    if img.mode != 'RGB' and img_format == 'JPEG':
        img = img.convert('RGB')
    
    # Redimensionner l'image si elle dépasse les dimensions maximales
    if img.width > MAX_WIDTH or img.height > MAX_HEIGHT:
        img.thumbnail((MAX_WIDTH, MAX_HEIGHT), Image.LANCZOS)
    
    # Créer un buffer pour stocker l'image optimisée
    output = io.BytesIO()
    
    # Enregistrer l'image avec compression
    if img_format == 'JPEG':
        img.save(output, format='JPEG', quality=85, optimize=True)
    else:  # PNG
        img.save(output, format='PNG', optimize=True)
    
    # Réinitialiser le pointeur du buffer
    output.seek(0)
    
    # Créer un nouvel objet de fichier à partir du buffer
    return InMemoryUploadedFile(
        output,
        'ImageField',
        f"{os.path.splitext(image_field.name)[0]}.{img_format.lower()}",
        f'image/{img_format.lower()}',
        output.getbuffer().nbytes,
        None
    )