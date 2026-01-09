from django.contrib.auth.password_validation import validate_password
from django_password_validators.password_character_requirements.password_validation import PasswordCharacterValidator
from django.core.exceptions import ValidationError

def validate_password_ptbr(password):
    """
    Validação com django validate_password
    com mensagens traduzidas
    """

    try:
        validate_password(password)
    except ValidationError as e:
        pcv = PasswordCharacterValidator()
        msgs_traduzidas = []
        for msg in e.messages:
            match msg:
                case texto if 'short' in texto:
                    msg = f'Esta senha é muito curta, ela deve conter pelo menos 8 dígitos'
                case texto if 'letter' in texto and not 'upper' in texto and not 'lower' in texto:
                    msg = f'A senha deve conter pelo menos 1 letra'
                case texto if 'digit' in texto:
                    msg = f'A senha deve conter pelo menos 1 número'
                case texto if 'upper' in texto:
                    msg = f'A senha deve conter pelo menos 1 letra maiúscula'
                case texto if 'lower' in texto:
                    msg = f'A senha deve conter pelo menos 1 letra minúscula'
                case texto if 'special' in texto:
                    msg = f'A senha deve conter pelo menos 1 caractere especial'
            msgs_traduzidas.append(msg)
        raise ValidationError(msgs_traduzidas)
