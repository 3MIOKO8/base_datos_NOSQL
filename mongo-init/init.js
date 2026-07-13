use("ComercioTech");

// Usuario de la aplicación
db.createUser({

    user: "app_gestion",

    pwd: "AppPassword2026",

    roles: [
        {
            role: "readWrite",
            db: "ComercioTech"
        }
    ]

});


// ==========================
// Colecciones
// ==========================

db.createCollection("clientes");

db.createCollection("productos");

db.createCollection("pedidos");

db.createCollection("contadores");


// ==========================
// Contadores iniciales
// ==========================

db.contadores.insertMany([

    {
        _id: "productos",
        ultimo_codigo: 0
    },

    {
        _id: "pedidos",
        ultimo_codigo: 0
    }

]);