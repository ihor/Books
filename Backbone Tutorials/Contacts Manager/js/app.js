(function ($) {
    var contacts = [
        { name: "Ihor Simpson", address: "742 Evergreen Terrace, Springfield", tel: "(911) 555-22-44", email: "ihor.j.fry@google.com", type: "family" },
        { name: "Antonina Simpson", address: "742 Evergreen Terrace, Springfield", tel: "(911) 444-33-22", email: "antonina.simpson@google.com", type: "family" },
        { name: "Julia Farnsworth", address: "Grand Central, New York", tel: "(911) 666-22-11", email: "julia.f@yahoo.com", type: "friend" },
        { name: "Bohdan Wong", address: "Hogwarts", tel: "(911) 222-33-11", email: "bohdan@wong.com", type: "colleague" },
        { name: "Alex Brannigan", address: "Somewhere in space", tel: "(911) 999-22-44", email: "al.bra@google.com", type: "family" },
        { name: "Viktor Flanders", address: "Golden Gate Bridge, San Francisco", tel: "(911) 333-33-22", email: "holy.viktor@google.com", type: "colleague" },
        { name: "Lyubov Lovejoy", address: "5 Avenue, New York", tel: "(911) 222-33-22", email: "love65@google.com", type: "friend" },
        { name: "Tetyana Skinner", address: "23 1st street, Springfield", tel: "(911) 111-88-77", email: "tetyana@math.edu", type: "family" }
    ];

    var Contact = Backbone.Model.extend({});

    var Directory = Backbone.Collection.extend({
        model: Contact
    });

    var ContactView = Backbone.View.extend({
        tagName: "article",
        className: "contact-container",
        template: $("#contactTemplate").html(),
        render: function () {
            var tmpl = _.template(this.template);
            this.$el.html(tmpl(this.model.toJSON()));
            return this;
        }
    });

    var DirectoryView = Backbone.View.extend({
        el: $("#contacts"),
        initialize: function () {
            this.collection = new Directory(contacts);
            this.render();
        },
        render: function () {
            var that = this;
            _.each(this.collection.models, function (item) {
                that.renderContact(item);
            }, this);
        },
        renderContact: function (item) {
            var contactView = new ContactView({
                model: item
            });
            this.$el.append(contactView.render().el);
        }
    });

    var directory = new DirectoryView();
} (jQuery));
