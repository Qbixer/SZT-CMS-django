SZT CMS Django
=======

Funkcjonalność
-----

CMS pozwala na dodawanie własnych podstron za pomocą sekcji i podsekcji automatycznie wyświetlanych na górnym pasku. Aby móc edytować CMS należy być adminem lub staff lub moderatorem. CMS pozwala na tworzenie stron za pomocą (aktualnie) 3 różnych komponentów: statycznej strony HTML, postów oraz modułu zapisu do newslettera. Administrator może zmieniać treść maili wysyłanych do użytkowników podczas rejestracji, zapisywania się do newslettera, a także ustawić jaka wiadomość powinna być dołączana do każdego maila z newslettera. Admin może także zmienić maila, z jakiego są wysyłane wiadomości.

---

Moduły
------

### account
Odpowiedzialny za uwierzytelnianie użytkownika

#### Modele
* Profile
  
  Służy do przetrzymywania dodatkowych informacji o użytkowniku

---

### main
Główny moduł odpowiedzialny za wyświetlanie informacji

#### Modele
* ContentType

  Zawiera listę typów komponentów możliwych do dodania. Konieczne ustawienie ich przed korzystaniem z CMS. Obecne wartości to:
    
    * post
    * newsletter
    * static
  
* MailConfiguration

  Zawiera konfigurację maila, z którego są wysyłane wiadomości. Konieczne ustawienie przed korzystaniem z CMS.

* EmailTemplate

  Zawiera szablony emaili wysyłanych przez CMS w trakcie jego działania. Konieczne ustawienie przed korzystaniem z CMS. Obecne wartości email_type to:

    * activate_newsletter
    * activate_account
    * deactivate_newsletter

* Section

  Opisuje podstawową kartę kategorii. Umożliwia stworzenie własnej podstrony.

* HomePage

  Parametry strony głównej

* PageLayout

  Jakie komponenty mają się wyświetlać na jakiej stronie

* Post

  Zawartość jednego postu dla danego pageLayoutu 'post'

* PostComment

  Komentarz do postu

* CustomHTML

  Zawartość pageLayoutu 'static'

---

### newsletter

Moduł odpowiedzialny za newsletter

#### Modele

* NewsletterUser

  Odpowiedzialny za zapisanie się użytkownika do newslettera

* EmailSent

  Przechowuje wysłane emaile

---

Instalacja
-----

Przed uruchomieniem CMS należy ściągnąć następujące rzeczy:
  * `pip install django`
  * `pip install django-ckeditor` - edytor WYSIWYG
  * `pip install Pillow` - biblioteka do przetwarzania zdjęć
  * `pip install django-photologue` - galeria zdjęć
  * `pip install pytz` - biblioteka do zarządzania czasem
  * `pip install social-auth-app-django` - component do logowania z innych źródeł
  * https://ckeditor.com/cke4/addon/youtube - addon do ckeditora

Następnie postawić postgresa i zmienić dane w blog/settings.py aby odpowiadały ustawieniom stworzonej bazy danych.

Dokonać migracji za pomocą polecenia `python manage.py migrate`.

Ustawić odpowienie dane w tabelach ContentType, EmailTemplate oraz MailConfiguration //TODO dodać to w migracji danych

Uruchomić serwer developerski za pomocą polecenia `python manage.py runserver`