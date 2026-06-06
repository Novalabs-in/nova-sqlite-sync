import pytest
import main

def test_offlinedbsync_instantiation():
    # Verify that the class OfflineDbSync is inspectable and loadable
    assert hasattr(main, 'OfflineDbSync')

