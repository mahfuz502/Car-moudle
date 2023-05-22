from email.policy import default

from odoo import models, fields, api


#                                                >car model<
class Car(models.Model):
    _name = "car.car"

    name = fields.Char(string='Name')
    horse_power = fields.Integer(string="Horse Power")
    door_number = fields.Integer(string="Doors Number")
    driver_id = fields.Many2one('res.partner', string="Driver")
    parking_id = fields.Many2one('parking.parking', string="Parking")
    feature_ids = fields.Many2many('car.feature', string="Features")
    total_speed = fields.Integer(string="Speed Total", compute="get_total_speed")
    random_message = fields.Char(string='Message', compute="say_hello")
    test = fields.Char(string='Test', compute="")
    image = fields.Image(string='Image')

    status = fields.Selection([('new', 'New'), ('used', 'Used'), ('sold', 'Sold')], string='Status', default='new')
    car_sequence = fields.Char(string='Sequence')
    sequence = fields.Integer(string="seq.")

    @api.model
    def create(self, vals):
        vals['car_sequence'] = self.env['ir.sequence'].next_by_code('car.sequence')
        result = super(Car, self).create(vals)
        return result

    #       <!-- button def -->
    def set_car_to_used(self):
        self.status = 'used'

    #       <!-- button def plus email -->
    def set_car_to_sold(self):
        self.status = 'sold'
        template_id = self.env.ref('aaa_first_module.car_mail_template')
        if template_id:
            template_id.send_mail(self.id, force_send=True, raise_exception=True,
                                  email_values={'email_to': self.driver_id.email})

    #       <!-- message def -->
    def say_hello(self):
        print("driver_id", self.driver_id)
        print("driver_id id", self.driver_id.id)
        print("driver_id name", self.driver_id.name)
        self.random_message = ' Hello' + self.driver_id.name

    #       <!-- speed def -->
    def get_total_speed(self):
        print("name", self.name)
        print("horse_power", self.horse_power)
        self.total_speed = self.horse_power * 50


# <!-- parking Model -->
class Parking(models.Model):
    _name = "parking.parking"

    name = fields.Char(string='Name')
    car_ids = fields.One2many('car.car', 'parking_id', string='Cars')


# <!-- Car Feature Model -->
class Car_Feature(models.Model):
    _name = "car.feature"

    name = fields.Char(string='Name')
    value = fields.Char(string='Value')
