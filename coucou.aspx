<%@ Page Language="C#" %>
<!DOCTYPE html>
<html>
<head>
    <title>Utilisation de variable en ASP.NET</title>
</head>
<body>
    <% 
        string nom = "Jean";
        Response.Write("<h1>Bonjour " + nom + " !</h1>");
    %>
</body>
</html>
