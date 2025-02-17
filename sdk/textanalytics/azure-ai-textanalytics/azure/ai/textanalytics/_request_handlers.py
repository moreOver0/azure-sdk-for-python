# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------


from ._generated.models import (
    EntitiesTask,
    PiiTask,
    EntityLinkingTask,
    SentimentAnalysisTask,
    ExtractiveSummarizationTask,
    CustomEntitiesTask,
    CustomSingleClassificationTask,
    CustomMultiClassificationTask,
)
from ._models import (
    DetectLanguageInput,
    TextDocumentInput,
    _AnalyzeActionsType,
)


def _validate_input(documents, hint, whole_input_hint):
    """Validate that batch input has either all string docs
    or dict/DetectLanguageInput/TextDocumentInput, not a mix of both.
    Assign country and language hints on a whole batch or per-item
    basis.

    :param list documents: The input documents.
    :return: A list of DetectLanguageInput or TextDocumentInput
    """
    if not documents:
        raise ValueError("Input documents can not be empty or None")

    if isinstance(documents, str):
        raise TypeError("Input documents cannot be a string.")

    if isinstance(documents, dict):
        raise TypeError("Input documents cannot be a dict")

    if not all(isinstance(x, str) for x in documents):
        if not all(
            isinstance(x, (dict, TextDocumentInput, DetectLanguageInput))
            for x in documents
        ):
            raise TypeError(
                "Mixing string and dictionary/object document input unsupported."
            )

    request_batch = []
    for idx, doc in enumerate(documents):
        if isinstance(doc, str):
            if hint == "country_hint" and whole_input_hint.lower() == "none":
                whole_input_hint = ""
            document = {"id": str(idx), hint: whole_input_hint, "text": doc}
            request_batch.append(document)
        if isinstance(doc, dict):
            item_hint = doc.get(hint, None)
            if item_hint is None:
                doc = {
                    "id": doc.get("id", None),
                    hint: whole_input_hint,
                    "text": doc.get("text", None),
                }
            elif item_hint.lower() == "none":
                doc = {
                    "id": doc.get("id", None),
                    hint: "",
                    "text": doc.get("text", None),
                }
            request_batch.append(doc)
        if isinstance(doc, TextDocumentInput):
            item_hint = doc.language
            if item_hint is None:
                doc = TextDocumentInput(
                    id=doc.id, language=whole_input_hint, text=doc.text
                )
            request_batch.append(doc)
        if isinstance(doc, DetectLanguageInput):
            item_hint = doc.country_hint
            if item_hint is None:
                doc = DetectLanguageInput(
                    id=doc.id, country_hint=whole_input_hint, text=doc.text
                )
            elif item_hint.lower() == "none":
                doc = DetectLanguageInput(id=doc.id, country_hint="", text=doc.text)
            request_batch.append(doc)

    return request_batch


def _determine_action_type(action):  # pylint: disable=too-many-return-statements
    if isinstance(action, EntitiesTask):
        return _AnalyzeActionsType.RECOGNIZE_ENTITIES
    if isinstance(action, PiiTask):
        return _AnalyzeActionsType.RECOGNIZE_PII_ENTITIES
    if isinstance(action, EntityLinkingTask):
        return _AnalyzeActionsType.RECOGNIZE_LINKED_ENTITIES
    if isinstance(action, SentimentAnalysisTask):
        return _AnalyzeActionsType.ANALYZE_SENTIMENT
    if isinstance(action, ExtractiveSummarizationTask):
        return _AnalyzeActionsType.EXTRACT_SUMMARY
    if isinstance(action, CustomEntitiesTask):
        return _AnalyzeActionsType.RECOGNIZE_CUSTOM_ENTITIES
    if isinstance(action, CustomSingleClassificationTask):
        return _AnalyzeActionsType.SINGLE_CATEGORY_CLASSIFY
    if isinstance(action, CustomMultiClassificationTask):
        return _AnalyzeActionsType.MULTI_CATEGORY_CLASSIFY
    return _AnalyzeActionsType.EXTRACT_KEY_PHRASES


def _check_string_index_type_arg(
    string_index_type_arg, api_version, string_index_type_default="UnicodeCodePoint"
):
    string_index_type = None

    if api_version == "v3.0":
        if string_index_type_arg is not None:
            raise ValueError(
                "'string_index_type' is only available for API version V3_1 and up"
            )

    else:
        if string_index_type_arg is None:
            string_index_type = string_index_type_default

        else:
            string_index_type = string_index_type_arg

    return string_index_type
