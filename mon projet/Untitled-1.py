import wx

class LoginPage(wx.Frame):
    def __init__(self, *args, **kw):
        super(LoginPage, self).__init__(*args, **kw)

        self.SetTitle("Login Page")
        self.SetSize((500, 400))

        # Panel principal
        panel = wx.Panel(self)

        # Sizer principal
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Barre de titre
        title_bar = wx.Panel(panel, size=(-1, 50))
        title_bar.SetBackgroundColour(wx.Colour(173, 216, 230))  # Couleur bleu clair
        title_sizer = wx.BoxSizer(wx.HORIZONTAL)
        title_text = wx.StaticText(title_bar, label="Login Page")
        title_sizer.AddStretchSpacer()
        title_sizer.Add(title_text, flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL, border=10)
        title_sizer.AddStretchSpacer()
        title_bar.SetSizer(title_sizer)

        main_sizer.Add(title_bar, flag=wx.EXPAND | wx.ALL, border=5)

        # Zone centrale avec l'avatar
        avatar_sizer = wx.BoxSizer(wx.HORIZONTAL)
        avatar_path = r"C:\\Users\\HP\\OneDrive\\Bureau\\téléchargement.png"   # Chemin avec une raw string
        avatar_image = wx.Image(avatar_path, wx.BITMAP_TYPE_PNG).Scale(100, 100, wx.IMAGE_QUALITY_HIGH)
        avatar_bitmap = wx.StaticBitmap(panel, bitmap=wx.Bitmap(avatar_image))
        avatar_sizer.AddSpacer(20)
        avatar_sizer.Add(avatar_bitmap, flag=wx.ALIGN_CENTER)
        avatar_sizer.AddSpacer(20)

        main_sizer.Add(avatar_sizer, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        # Champs utilisateur et mot de passe
        form_sizer = wx.FlexGridSizer(2, 2, 10, 10)
        form_sizer.AddGrowableCol(1, 1)

        username_label = wx.StaticText(panel, label="Username:")
        self.username_input = wx.TextCtrl(panel)
        form_sizer.Add(username_label, flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.username_input, flag=wx.EXPAND)

        password_label = wx.StaticText(panel, label="Password:")
        self.password_input = wx.TextCtrl(panel, style=wx.TE_PASSWORD)
        form_sizer.Add(password_label, flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
        form_sizer.Add(self.password_input, flag=wx.EXPAND)

        main_sizer.Add(form_sizer, flag=wx.EXPAND | wx.ALL, border=10)

        # Boutons de connexion et d'inscription
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        login_button = wx.Button(panel, label="Login")
        login_button.Bind(wx.EVT_BUTTON, self.on_login)
        signup_button = wx.Button(panel, label="Sign Up")
        signup_button.Bind(wx.EVT_BUTTON, self.on_signup)
        button_sizer.Add(login_button, flag=wx.RIGHT, border=10)
        button_sizer.Add(signup_button)

        main_sizer.Add(button_sizer, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        panel.SetSizer(main_sizer)

        # Stocker les utilisateurs enregistrés (persistants)
        if not hasattr(LoginPage, 'users'):
            LoginPage.users = {}
        if not hasattr(LoginPage, 'user_details'):
            LoginPage.user_details = []

    def on_login(self, event):
        username = self.username_input.GetValue()
        password = self.password_input.GetValue()

        # Vérification des informations d'identification enregistrées
        if username == "admin" and password == "admin":
            wx.MessageBox("Bienvenue, admin!", "Succès", wx.OK | wx.ICON_INFORMATION)
            self.show_admin_page()
        elif username in LoginPage.users and LoginPage.users[username] == password:
            wx.MessageBox("Bienvenue, {}!".format(username), "Succès", wx.OK | wx.ICON_INFORMATION)
            self.show_welcome_page()
        else:
            wx.MessageBox("Nom d'utilisateur ou mot de passe incorrect!", "Erreur", wx.OK | wx.ICON_ERROR)

    def on_signup(self, event):
        signup_frame = SignupPage(LoginPage.users, LoginPage.user_details, None)
        signup_frame.Show()
        self.Close()

    def show_welcome_page(self):
        welcome_frame = WelcomePage(None)
        welcome_frame.Show()
        self.Close()

    def show_admin_page(self):
        admin_frame = AdminPage(LoginPage.user_details, None)
        admin_frame.Show()
        self.Close()

class SignupPage(wx.Frame):
    def __init__(self, users, user_details, *args, **kw):
        super(SignupPage, self).__init__(*args, **kw)

        self.users = users
        self.user_details = user_details

        self.SetTitle("Sign Up Page")
        self.SetSize((500, 600))

        panel = wx.Panel(self)
        main_sizer = wx.BoxSizer(wx.VERTICAL)

        # Champs de création de compte
        form_sizer = wx.FlexGridSizer(7, 2, 10, 10)
        form_sizer.AddGrowableCol(1, 1)

        fields = [
            ("Nom:", wx.TextCtrl(panel)),
            ("Prénom:", wx.TextCtrl(panel)),
            ("Username:", wx.TextCtrl(panel)),
            ("Numéro:", wx.TextCtrl(panel)),
            ("Email:", wx.TextCtrl(panel)),
            ("Mot de passe:", wx.TextCtrl(panel, style=wx.TE_PASSWORD)),
            ("Confirmer mot de passe:", wx.TextCtrl(panel, style=wx.TE_PASSWORD)),
        ]

        self.inputs = {}
        for label, ctrl in fields:
            form_sizer.Add(wx.StaticText(panel, label=label), flag=wx.ALIGN_RIGHT | wx.ALIGN_CENTER_VERTICAL)
            form_sizer.Add(ctrl, flag=wx.EXPAND)
            self.inputs[label] = ctrl

        main_sizer.Add(form_sizer, flag=wx.EXPAND | wx.ALL, border=10)

        # Checkbox d'acceptation des règles
        self.checkbox = wx.CheckBox(panel, label="J'accepte le règlement en vigueur")
        main_sizer.Add(self.checkbox, flag=wx.ALIGN_LEFT | wx.ALL, border=10)

        # Bouton d'enregistrement
        button_sizer = wx.BoxSizer(wx.HORIZONTAL)
        register_button = wx.Button(panel, label="Enregistrer")
        register_button.Bind(wx.EVT_BUTTON, self.on_register)
        button_sizer.Add(register_button)

        back_button = wx.Button(panel, label="Retour")
        back_button.Bind(wx.EVT_BUTTON, self.on_back)
        button_sizer.Add(back_button, flag=wx.LEFT, border=10)

        main_sizer.Add(button_sizer, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        panel.SetSizer(main_sizer)

    def on_register(self, event):
        # Vérifier que tous les champs sont remplis
        for label, ctrl in self.inputs.items():
            if not ctrl.GetValue().strip():
                wx.MessageBox(f"Le champ '{label}' est requis.", "Erreur", wx.OK | wx.ICON_ERROR)
                return

        # Vérifier que les mots de passe correspondent
        password = self.inputs["Mot de passe:"].GetValue()
        confirm_password = self.inputs["Confirmer mot de passe:"].GetValue()
        if password != confirm_password:
            wx.MessageBox("Les mots de passe ne correspondent pas.", "Erreur", wx.OK | wx.ICON_ERROR)
            return

        # Vérifier que la case est cochée
        if not self.checkbox.IsChecked():
            wx.MessageBox("Vous devez accepter le règlement pour créer un compte.", "Erreur", wx.OK | wx.ICON_ERROR)
            return

        username = self.inputs["Username:"].GetValue()

        # Vérifier si le username existe déjà
        if username in self.users:
            wx.MessageBox("Ce nom d'utilisateur est déjà pris.", "Erreur", wx.OK | wx.ICON_ERROR)
            return

        # Enregistrer l'utilisateur
        self.users[username] = password
        user_info = {label: ctrl.GetValue() for label, ctrl in self.inputs.items() if label != "Confirmer mot de passe:"}
        self.user_details.append(user_info)
        wx.MessageBox("Compte créé avec succès!", "Succès", wx.OK | wx.ICON_INFORMATION)
        self.on_back(None)

    def on_back(self, event):
        login_frame = LoginPage(None)
        login_frame.Show()
        self.Close()

class WelcomePage(wx.Frame):
    def __init__(self, *args, **kw):
        super(WelcomePage, self).__init__(*args, **kw)

        self.SetTitle("Welcome Page")
        self.SetSize((400, 300))

        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)

        welcome_text = wx.StaticText(panel, label="Bienvenue sur la page principale!")
        font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        welcome_text.SetFont(font)

        sizer.Add(welcome_text, flag=wx.ALIGN_CENTER | wx.ALL, border=20)

        # Bouton de déconnexion
        logout_button = wx.Button(panel, label="Se déconnecter")
        logout_button.Bind(wx.EVT_BUTTON, self.on_logout)
        sizer.Add(logout_button, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        panel.SetSizer(sizer)

    def on_logout(self, event):
        login_frame = LoginPage(None)
        login_frame.Show()
        self.Close()

class AdminPage(wx.Frame):
    def __init__(self, user_details, *args, **kw):
        super(AdminPage, self).__init__(*args, **kw)

        self.user_details = user_details

        self.SetTitle("Admin Page")
        self.SetSize((600, 400))

        panel = wx.Panel(self)
        self.panel = panel  # Stocker une référence au panel
        sizer = wx.BoxSizer(wx.VERTICAL)

        title = wx.StaticText(panel, label="Liste des utilisateurs enregistrés")
        font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)
        title.SetFont(font)
        sizer.Add(title, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        # Tableau des utilisateurs
        self.grid_sizer = wx.FlexGridSizer(rows=len(user_details) + 1, cols=6, hgap=10, vgap=10)
        headers = ["Nom", "Prénom", "Username", "Numéro", "Email", "Action"]

        for header in headers:
            self.grid_sizer.Add(wx.StaticText(panel, label=header, style=wx.ALIGN_CENTER), flag=wx.EXPAND)

        self.populate_table(panel)

        sizer.Add(self.grid_sizer, flag=wx.EXPAND | wx.ALL, border=10)

        # Bouton de déconnexion
        logout_button = wx.Button(panel, label="Se déconnecter")
        logout_button.Bind(wx.EVT_BUTTON, self.on_logout)
        sizer.Add(logout_button, flag=wx.ALIGN_CENTER | wx.ALL, border=10)

        panel.SetSizer(sizer)

    def populate_table(self, panel):
        for user in self.user_details:
            self.grid_sizer.Add(wx.StaticText(panel, label=user.get("Nom:", "")))
            self.grid_sizer.Add(wx.StaticText(panel, label=user.get("Prénom:", "")))
            self.grid_sizer.Add(wx.StaticText(panel, label=user.get("Username:", "")))
            self.grid_sizer.Add(wx.StaticText(panel, label=user.get("Numéro:", "")))
            self.grid_sizer.Add(wx.StaticText(panel, label=user.get("Email:", "")))
            delete_button = wx.Button(panel, label="Supprimer")
            delete_button.Bind(wx.EVT_BUTTON, lambda event, u=user: self.delete_user(u))
            self.grid_sizer.Add(delete_button)

    def delete_user(self, user):
        username = user.get("Username:")
        if username in LoginPage.users:
            del LoginPage.users[username]
        if user in self.user_details:
            self.user_details.remove(user)
        wx.MessageBox(f"Utilisateur {username} supprimé.", "Succès", wx.OK | wx.ICON_INFORMATION)
        self.refresh_table()

    def refresh_table(self):
        for child in self.grid_sizer.GetChildren():
            child.GetWindow().Destroy() if child.GetWindow() else None
        self.grid_sizer.Clear()

        headers = ["Nom", "Prénom", "Username", "Numéro", "Email", "Action"]
        for header in headers:
            self.grid_sizer.Add(wx.StaticText(self.panel, label=header, style=wx.ALIGN_CENTER), flag=wx.EXPAND)

        self.populate_table(self.panel)
        self.Layout()

    def on_logout(self, event):
        login_frame = LoginPage(None)
        login_frame.Show()
        self.Close()

if __name__ == "__main__":
    app = wx.App(False)
    frame = LoginPage(None)
    frame.Show()
    app.MainLoop()
