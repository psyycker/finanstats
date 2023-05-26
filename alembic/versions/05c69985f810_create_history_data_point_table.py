"""create history data point table

Revision ID: 05c69985f810
Revises: 9e08b66c5e56
Create Date: 2023-05-26 19:12:57.014418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '05c69985f810'
down_revision = '9e08b66c5e56'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "history_data_points",
        sa.Column("ticker", sa.String, primary_key=True),
        sa.Column("date", sa.Date, primary_key=True),
        sa.Column("open", sa.Float),
        sa.Column("close", sa.Float),
        sa.Column("high", sa.Float),
        sa.Column("low", sa.Float),
        sa.Column("volume", sa.Numeric)
    )


def downgrade() -> None:
    pass
