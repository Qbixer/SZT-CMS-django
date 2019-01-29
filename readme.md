SZT CMS Django
=======

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




