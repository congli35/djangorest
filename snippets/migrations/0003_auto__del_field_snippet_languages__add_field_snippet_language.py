# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Snippet.languages'
        db.delete_column(u'snippets_snippet', 'languages')

        # Adding field 'Snippet.language'
        db.add_column(u'snippets_snippet', 'language',
                      self.gf('django.db.models.fields.CharField')(default='python', max_length=100),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Snippet.languages'
        db.add_column(u'snippets_snippet', 'languages',
                      self.gf('django.db.models.fields.CharField')(default='python', max_length=100),
                      keep_default=False)

        # Deleting field 'Snippet.language'
        db.delete_column(u'snippets_snippet', 'language')


    models = {
        u'snippets.snippet': {
            'Meta': {'ordering': "set(['created'])", 'object_name': 'Snippet'},
            'code': ('django.db.models.fields.TextField', [], {}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'language': ('django.db.models.fields.CharField', [], {'default': "'python'", 'max_length': '100'}),
            'linenos': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'style': ('django.db.models.fields.CharField', [], {'default': "'friendly'", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100', 'blank': 'True'})
        }
    }

    complete_apps = ['snippets']