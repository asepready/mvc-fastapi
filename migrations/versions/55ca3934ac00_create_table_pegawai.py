"""create table pegawai

Revision ID: 55ca3934ac00
Revises: 
Create Date: 2021-12-06 18:57:49.312948

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '55ca3934ac00'
down_revision = None
branch_labels = None
depends_on = None

from faker import Faker
faker = Faker('id')

def upgrade():
    pgw = op.create_table('tb_pegawai',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nama_pegawai', sa.String(255), nullable=False),
        sa.Column('alamat_pegawai', sa.String(255)),
        sa.Column('ttl_pegawai', sa.Date()),
        sa.Column('telp_pegawai', sa.String(255)),
        sa.Column('email_pegawai', sa.String(255), unique=True)
    )
    op.bulk_insert(
        pgw,
        [{
            'nama_pegawai':faker.name(), 
            'alamat_pegawai':faker.address(),
            'ttl_pegawai':faker.date_of_birth(tzinfo=None, minimum_age=21, maximum_age=28),
            'telp_pegawai':faker.phone_number(),
            'email_pegawai':faker.email()
        }for x in range(800)]
    )

def downgrade():
    op.drop_table('tb_pegawai')
