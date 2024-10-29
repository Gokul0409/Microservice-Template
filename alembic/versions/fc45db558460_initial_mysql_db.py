"""Initial MySQL DB

Revision ID: fc45db558460
Revises:
Create Date: 2024-10-29 15:02:42.613753

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fc45db558460'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('people',
                    sa.Column('sn', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(50), nullable=False),
                    sa.PrimaryKeyConstraint('sn')
                    )


def downgrade() -> None:
    op.drop_table('people')
