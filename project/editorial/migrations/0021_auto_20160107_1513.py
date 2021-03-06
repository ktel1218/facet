# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editorial', '0020_privatemessage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='audiofacet',
            name='status',
            field=models.CharField(help_text=b'Audiofacet status choice.', max_length=25, choices=[(b'DRFT', b'Draft'), (b'PT', b'Pitch'), (b'IP', b'In Progress'), (b'EDT', b'Edit'), (b'RVN', b'Revision'), (b'NR', b'Needs Review'), (b'RDY', b'Ready')]),
        ),
        migrations.AlterField(
            model_name='historicalaudiofacet',
            name='status',
            field=models.CharField(help_text=b'Audiofacet status choice.', max_length=25, choices=[(b'DRFT', b'Draft'), (b'PT', b'Pitch'), (b'IP', b'In Progress'), (b'EDT', b'Edit'), (b'RVN', b'Revision'), (b'NR', b'Needs Review'), (b'RDY', b'Ready')]),
        ),
        migrations.AlterField(
            model_name='historicalprintfacet',
            name='status',
            field=models.CharField(help_text=b'Printfacet status choice.', max_length=25, choices=[(b'DRFT', b'Draft'), (b'PT', b'Pitch'), (b'IP', b'In Progress'), (b'EDT', b'Edit'), (b'RVN', b'Revision'), (b'NR', b'Needs Review'), (b'RDY', b'Ready')]),
        ),
        migrations.AlterField(
            model_name='historicalvideofacet',
            name='status',
            field=models.CharField(help_text=b'Videofacet status choice.', max_length=25, choices=[(b'DRFT', b'Draft'), (b'PT', b'Pitch'), (b'IP', b'In Progress'), (b'EDT', b'Edit'), (b'RVN', b'Revision'), (b'NR', b'Needs Review'), (b'RDY', b'Ready')]),
        ),
        migrations.AlterField(
            model_name='historicalwebfacet',
            name='status',
            field=models.CharField(help_text=b'WebFacet status choice.', max_length=25, choices=[(b'DRFT', b'Draft'), (b'PT', b'Pitch'), (b'IP', b'In Progress'), (b'EDT', b'Edit'), (b'RVN', b'Revision'), (b'NR', b'Needs Review'), (b'RDY', b'Ready')]),
        ),
        migrations.AlterField(
            model_name='printfacet',
            name='status',
            field=models.CharField(help_text=b'Printfacet status choice.', max_length=25, choices=[(b'DRFT', b'Draft'), (b'PT', b'Pitch'), (b'IP', b'In Progress'), (b'EDT', b'Edit'), (b'RVN', b'Revision'), (b'NR', b'Needs Review'), (b'RDY', b'Ready')]),
        ),
        migrations.AlterField(
            model_name='printfacetcopydetail',
            name='new_printfacet_id',
            field=models.SlugField(help_text=b"Id of the print on the copying organization's site.", max_length=15),
        ),
        migrations.AlterField(
            model_name='printfacetcopydetail',
            name='original_printfacet_id',
            field=models.ForeignKey(help_text=b'Original id of the facet.', to='editorial.PrintFacet'),
        ),
        migrations.AlterField(
            model_name='videofacet',
            name='status',
            field=models.CharField(help_text=b'Videofacet status choice.', max_length=25, choices=[(b'DRFT', b'Draft'), (b'PT', b'Pitch'), (b'IP', b'In Progress'), (b'EDT', b'Edit'), (b'RVN', b'Revision'), (b'NR', b'Needs Review'), (b'RDY', b'Ready')]),
        ),
        migrations.AlterField(
            model_name='webfacet',
            name='status',
            field=models.CharField(help_text=b'WebFacet status choice.', max_length=25, choices=[(b'DRFT', b'Draft'), (b'PT', b'Pitch'), (b'IP', b'In Progress'), (b'EDT', b'Edit'), (b'RVN', b'Revision'), (b'NR', b'Needs Review'), (b'RDY', b'Ready')]),
        ),
        migrations.AlterField(
            model_name='webfacetcopydetail',
            name='new_webfacet_id',
            field=models.SlugField(help_text=b"Id of the webfacet on the copying organization's site.", max_length=15),
        ),
        migrations.AlterField(
            model_name='webfacetcopydetail',
            name='original_webfacet_id',
            field=models.ForeignKey(help_text=b'Original id of the facet.', to='editorial.WebFacet'),
        ),
    ]
