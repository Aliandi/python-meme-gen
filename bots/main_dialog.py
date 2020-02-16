from botbuilder.dialogs import (
    ComponentDialog,
    WaterfallDialog,
    WaterfallStepContext,
    DialogTurnResult,
    TextPrompt, PromptOptions)
from botbuilder.core import MessageFactory, UserState
from botbuilder.schema import CardAction, SuggestedActions, ActionTypes

from api.meme_processor import MemeProcessor
from api.meme_requests import MemeRequests
from bots import activity_helper
from meme import Meme


class MainDialog(ComponentDialog):
    def __init__(self, user_state: UserState):
        super(MainDialog, self).__init__(MainDialog.__name__)

        self.user_state = user_state
        self.add_dialog(
            WaterfallDialog("WFDialog", [self.help_step, self.final_step])
        )
        self.add_dialog(TextPrompt(TextPrompt.__name__))

        self.initial_dialog_id = "WFDialog"

    async def help_step(self, step_context: WaterfallStepContext):
        actions = SuggestedActions(
            actions=[
                CardAction(title="Key", type=ActionTypes.im_back, value="key"),
                CardAction(title="ID", type=ActionTypes.im_back, value="id"),
            ]
        )
        response = activity_helper.create_activity_reply(
            step_context.context.activity,
            "To use this bot simply tell me the ID or any keyword and I'll try to find it",'', actions
        )

        return await step_context.prompt(
            TextPrompt.__name__, PromptOptions(prompt=response)
        )

    async def final_step(self, step_context: WaterfallStepContext) -> DialogTurnResult:
        user_input = str(step_context.result)

        meme_data = user_input.split(',')

        possible_memes = MemeProcessor.get_meme_by_keyword(meme_data[0])
        created_meme = MemeRequests.create_meme(possible_memes[0].id, meme_data[1], meme_data[2])['data']['url']
        #await step_context.context.send_activity(MessageFactory.text(f'Your created meme can be found at: {created_meme}'))
        await step_context.context.send_activity(MessageFactory.text(
            f'Your created meme can be found at: {created_meme}'))

        return await step_context.end_dialog()