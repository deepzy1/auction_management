from pkg_resources import require
import random
import logging
from odoo import api,models,fields,_
from odoo.exceptions import ValidationError
from datetime import datetime, timedelta
_logger = logging.getLogger(__name__)

class NewUser(models.Model):
    _name = "auction.user"
    _description = "User information"

    name = fields.Char(string='Full Name', required=True)
    email = fields.Char(string='Email', required=True, unique=True)
    password = fields.Char(string='Password', required=True)
    phone = fields.Char(string='Phone')
    address = fields.Text(string='Address')
    active = fields.Boolean(string='Active', default=True)
    bid_id=fields.Many2one('bid.logs', string="Bid")



    _sql_constraints = [
        ('email_unique','unique(email)','The email must be unique.'),
    ]

    def _check_email_format(self):
        for record in self:
            if not record.email or '@' not in record.email:
                raise ValidationError(_("Please provide a valid email address"))

    def check_credentials(self,email,password):
        user = self.search([('email','=',email),('password','=',password)],limit=1)
        return user if user else None
    
   
        
class UserRegisterOtp(models.Model):
    _name="user.register.otp"
    _description="User Otp"

    email=fields.Char(string="Email")
    otp = fields.Char(string='OTP')  # Temporary field for storing OTP
    expire_time=fields.Datetime(string="Expire Time", required=True)
    otp_verified = fields.Boolean(string='OTP Verified', default=False)


    @api.model
    def generate_otp(self,email):
        try:
            otp=random.randint(100000,999999)

            expire_time=datetime.now()+timedelta(minutes=5)

             # Create or update the OTP record for the email
            existing_otp=self.search([('email', '=', email)], limit=1)
            if existing_otp:
                existing_otp.write({'otp':otp, 'expire_time':expire_time})
            else:
                self.create({'otp':otp, 'expire_time':expire_time,'email': email})

            # Send OTP via email
            self.env['mail.mail'].create({
                'subject': 'Your OTP for Auction Registration',
                'email_to': email,
                'body_html': f"""
                    <p>Hello,</p>
                    <p>Your OTP for registration is: <strong>{otp}</strong></p>
                    <p>This OTP is valid for 5 minutes.</p>
                """,
                'email_from': self.env.user.email,
            }).send()

            return True
        
        except Exception as e:
            _logger.error(f"Error generating OTP for {email}: {e}")
            return False