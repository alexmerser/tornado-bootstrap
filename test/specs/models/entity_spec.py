# Copyright (c) 2010 Pedro Matiello <pmatiello@gmail.com>

from mockito import any, mock, verify, when
from models.entity import entity, entity_repository
import config.database

class entity_repository_spec():

    def setup(self):
        self.session = mock()
        self.repository = entity_repository(self.session)
        self.msg = entity("Field1 data", "Field1 data")
    
    def should_load_entities(self):
        query = mock()
        filtered_query = mock()
        when(self.session).query(entity).thenReturn(query)
        when(query).filter(any()).thenReturn(filtered_query)
        when(filtered_query).first().thenReturn(self.msg)
        assert self.repository.load(1) == self.msg
    
    def should_save_entities(self):
        self.repository.save(self.msg)
        verify(self.session).add(self.msg)
        verify(self.session).commit()
    
    def should_delete_entities(self):
        self.repository.remove(self.msg)
        verify(self.session).delete(self.msg)
        verify(self.session).commit()
    
    def should_list_entitities(self):
        query = mock()
        when(self.session).query(entity).thenReturn(query)
        when(query).all().thenReturn([self.msg])
        assert self.repository.list() == [self.msg]